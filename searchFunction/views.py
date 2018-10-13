from django.shortcuts import render
from .models import Investigator
from .models import Publication
from .models import Grant
from .models import terms_list
from .models import author2citation
from .models import term_vectors
from .models import author_grant_vectors
from .models import grant_documents
from .models import authors_grants_pairwise_cosine_similarity_matrix
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.views.decorators.cache import cache_page
import pygal
from django.views.generic import TemplateView
from .charts import MeshChart, AuthorChart

#@cache_page(60 * 10080)
def index(request):
	return render(request, 'searchFunction/index.html',{})

def results(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		grants = Grant.objects.filter(title__icontains=search_query).values('title', 'expiryDate', "guidelink", "openDate", "parentFOA", "agency")
		profiles = Investigator.objects.all()
		return render(request, 'searchFunction/results.html',{'grants': grants, 'profiles' : profiles}) #the render method is essentially what passes variables into the html templates.

#Here we have the term matched to it's vector, 
#then take the vectors and iterate through all author/grant vectors and find the cos value for each combination 

def LSI(request):
	if request.method == 'GET':
		LSI_search_query = request.GET.get('search_box', None)
		tl = terms_list.objects.filter(term__icontains=LSI_search_query).values_list('id')#Search term lookup
		termVectorQS = term_vectors.objects.filter(pk__in=tl).values()#match searched terms to vectors
		termList = [] #temp lists to hold string lists until float conversion is done.
		agvList = []
		agvResults = {}
		for vectorList in termVectorQS:
			termList.append(list(map(float, vectorList['termVector'].split())))#Convert the vector strings to a list of floats

		agv = author_grant_vectors.objects.values()
		for t in agv:
			agvList.append(list(map(float, t['grantvector'].split())))#Convert the vector strings to a list of floats


		for x in termList:#This is the main LSA function, it goes through the list of termvectors from the users search, finds the cosine sim with each author/grant vector and stores them in agvResults.
			count = 0 #The count is to match each cosine similarity with the sql ID of each author grant that it belongs to (as seen in termVectorsFiltered)
			for y in agvList:
				count+=1
				if cosine_similarity([x],[y])[0][0]>.1: #The number here is the threshold for whether or not results are displayed. I'd like to have a slider bar in the UI later on so that users can narrow or expand the results dynamically.
					agvResults[count] = cosine_similarity([x],[y])[0][0]
		
		g = agvResults.keys()
		termVectorsFiltered = author_grant_vectors.objects.filter(id__in=g)
		Authors = termVectorsFiltered.filter(item__contains='Author')
		authorsFiltered = termVectorsFiltered.filter(item__contains='Author').values_list('item')
		grantsFiltered = termVectorsFiltered.filter(item__contains='Grant').values_list('item')
		profiles = Investigator.objects.filter(investigator_tag__in=authorsFiltered).values()
		Grants = grant_documents.objects.filter(grantID__in=grantsFiltered).values()

		return render(request, 'searchFunction/LSI.html',{'Authors' :  Authors, 'Grants' :  Grants, 'profiles' : profiles, 'agvResults' : agvResults})

def profile(request):
	if request.method == 'GET':
		profiles = Investigator.objects.all()
		return render(request, 'searchFunction/profile.html',{'profiles' : profiles})

def userprofile(request): 
	citationList = []
	if request.method == 'GET':
		p=(request.GET.get('investigator_tag'))
		Grants = grant_documents.objects.all()
		#The p[7:] is here to slice the "Author_" part off of the author tags, as the author tag in author2citation does not contain the "Author_" prefix
		citations = author2citation.objects.values().filter(author__exact=p[7:])
		for cList in citations:
			citationList=(list(map(int, cList['citation_id'].split(","))))
		publications = Publication.objects.filter(pmid__in=citationList)
		profiles = Investigator.objects.filter(investigator_tag__exact=p)
		simAll = authors_grants_pairwise_cosine_similarity_matrix.objects.filter(x_axis__contains=p).filter(cosine_score__gt=.2).exclude(y_axis=p)
		simGrants = simAll.filter(y_axis__contains='Grant').order_by('-cosine_score').distinct()
		simAuthors = simAll.filter(y_axis__contains='Author').order_by('-cosine_score').distinct()
		# grantInfo = grant_documents.objects.filter(grantID__in=simGrants.values('y_axis')).distinct()
		# authorInfo = Investigator.objects.filter(investigator_tag__in=simAuthors.values('y_axis')).distinct() 
		MeshChart.chart(publications)
		AuthorChart.chart(publications)
		return render(request, 'searchFunction/userprofile.html', {'profiles' : profiles, 'simGrants' : simGrants, 'simAuthors' : simAuthors, 'publications':publications} )


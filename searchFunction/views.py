from django.shortcuts import render
from .models import Investigator
from .models import Grant
from .models import terms_list
from .models import term_vectors
from .models import author_grant_vectors
from .models import authors_grants_pairwise_cosine_similarity_matrix
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import FloatField
from django.db.models.functions import Cast
from scipy import spatial

def index(request):
	return render(request, 'searchFunction/index.html',{})

def results(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		grants = Grant.objects.filter(title__icontains=search_query).values('title', 'expiryDate', "guidelink", "openDate", "parentFOA", "agency")
		profiles = Investigator.objects.all()
		return render(request, 'searchFunction/results.html',{'grants': grants, 'profiles' : profiles})


#Here have the term matched to it's vector, 
#then take the vectors and iterate through all author/grant vectors and find the cos value for each combination 


def LSI(request):
	if request.method == 'GET':
		LSI_search_query = request.GET.get('search_box', None)
		tl = terms_list.objects.filter(term__icontains=LSI_search_query)
		tv = term_vectors.objects.all()
		termVectorQS = tv.filter(pk__in=tl).values()
		termList = [] #temp lists to hold string lists until float conversion is done.
		agvList = []
		agvResults = {}
		for vectorList in termVectorQS:
			termList.append(list(map(float, vectorList['termVector'].split())))#Convert the vector strings to floats

		agv = author_grant_vectors.objects.values()
		for t in agv:
			agvList.append(list(map(float, t['grantvector'].split())))#Convert the vector strings to floats
		
		for x in termList:#This is the main LSA function, it goes through the list of termvectors from the users search, finds the cosine sim with each author/grant vector and stores them in agvResults.
			count = 0 #The count is to match each cosine similarity with the sql ID of each author grant that it belongs to (as seen in termVectorsFiltered)
			for y in agvList:
				count+=1
				if cosine_similarity([x],[y])[0][0]>.1: #The .1 here is the threshold for whether or not results are displayed. I'd like to have a slider bar in the UI later on so that users can narrow or expand the results dynamically.
					agvResults[count] = cosine_similarity([x],[y])[0][0]
		
		g = agvResults.keys()
		termVectorsFiltered = author_grant_vectors.objects.filter(id__in=g)
		termVectors = termVectorsFiltered.values()
		Authors = termVectorsFiltered.filter(item__contains='Author')
		authorsFiltered = termVectorsFiltered.filter(item__contains='Author').values_list('item')
		Grants = termVectorsFiltered.filter(item__contains='Grant')
		profiles = Investigator.objects.filter(investigator_tag__in=authorsFiltered).values()#I broke this when I updated the investigator table somehow. It seems like its not finding any matches in authorsFiltered?

			

		return render(request, 'searchFunction/LSI.html',{'Authors' :  Authors, 'Grants' :  Grants, 'profiles' : profiles, 'agvResults' : agvResults})

def profile(request):
	if request.method == 'GET':
		profiles = Investigator.objects.all()
		return render(request, 'searchFunction/profile.html',{'profiles' : profiles})




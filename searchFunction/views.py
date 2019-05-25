from django.shortcuts import render
from .models import Investigator
from .models import Publication
from .models import Grant
from .models import ClinicalTrial
from .models import terms_list
from .models import items_list
from .models import similarity_matrix
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.views.decorators.cache import cache_page
import pygal
from django.views.generic import TemplateView
from .charts import MeshChart, AuthorChart, PublicationHistoryChart
from django.http import Http404

#@cache_page(60 * 10080)

def index(request):
	return render(request, 'searchFunction/index.html',{})

#TODO: some tables are queried twice, can be simplified to increase performance
def results(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		Grants = Grant.objects.annotate(rank=SearchRank(SearchVector('title', weight='A')+SearchVector('grantText', weight='B'), search_query)).filter(rank__gte=0.01).order_by('-rank')
		publications = Publication.objects.filter(title__icontains=search_query) | Publication.objects.filter(abstract__icontains=search_query)
		profiles = Investigator.objects.filter(fullName__icontains=search_query) | Investigator.objects.filter(investigator_tag__in=publications.values('investigator_tag'))
		ClinicalTrials = ClinicalTrial.objects.filter(title__icontains=search_query).annotate(rank=SearchRank(SearchVector('title', weight='A'), search_query)).filter(rank__gte=0.01).order_by('-rank')
		querySize = ClinicalTrials.count() + profiles.count() + Grants.count()
		g = Grants.values()
		return render(request, 'searchFunction/results.html',{'Grants' : Grants, 'profiles' : profiles, 'ClinicalTrials' : ClinicalTrials, 'query': search_query, 'size' : querySize}) 


#Here we have the term matched to its vector, then take the vectors and iterate through all author/grant vectors and find the cos value for each combination dynamically
def LSI(request):
	if request.method == 'GET':
		t=[]
		LSI_search_query = request.GET.get('search_box', None)
		preterm = LSI_search_query.split(' ')
		for a in preterm:
			t.append(a.lower())
		termVectorQS = terms_list.objects.filter(term__in=t)#match searched terms to vectors
		if not termVectorQS:
			raise Http404("No match found for your query")
		termVectors = [[sum(x) for x in zip(*termVectorQS.values_list('termVector', flat=True))]]
		items = items_list.objects.all()
		cosDict = {}

		#creates a list of all cosine scores between the term vector and all item vectors
		cos = list(cosine_similarity(termVectors,items.values_list('itemVector', flat=True))[0])

		#maps all cosine scores to their respective indexKeys
		for x in cos:
			cosDict[cos.index(x)+1] = x

		#copy any cos values over .1 to a copy of the dict, effectively removing very low similarity scores
		cosDict = { k : "{:.2f}".format(v) for k,v in cosDict.items() if v>.1}
		dictSize = len(cosDict)
		#indexKey lookups to fetch matching items
		profiles = Investigator.objects.filter(indexKey__in=cosDict.keys())
		Grants = Grant.objects.filter(indexKey__in=cosDict.keys())
		ClinicalTrials = ClinicalTrial.objects.filter(indexKey__in=cosDict.keys())

		return render(request, 'searchFunction/LSI.html',{'Grants' : Grants, 'profiles': profiles, 'ClinicalTrials' : ClinicalTrials, 'cosDict' : cosDict, 'query': LSI_search_query, 'size' : dictSize})

#TODO: Finish this
def browse(request):
	if request.method == 'GET':
		Grants = Grant.objects.all()
		ClinicalTrials = ClinicalTrial.objects.all()
		profiles = Investigator.objects.all()
		querySize = ClinicalTrials.count() + profiles.count() + Grants.count()

		return render(request, 'searchFunction/browse.html',{'Grants' : Grants, 'profiles': profiles, 'ClinicalTrials' : ClinicalTrials, 'size' : querySize})

#TODO: Investigator table is queried twice here, call Investigator.all() once then query that to increase performance!

def userprofile(request): 
	if request.method == 'GET':
		p=(request.GET.get('investigator_tag'))
		profiles = Investigator.objects.filter(investigator_tag__exact=p)
		publications = Publication.objects.filter(investigator_tag__contains=p)#slice "author_" off to match inconsistent publication tagging
		simAll = similarity_matrix.objects.filter(y_axis__in=profiles).filter(cosine_score__gt=0)
		simGrants = Grant.objects.filter(indexKey__in=simAll.values('x_axis'))
		simAuthors = Investigator.objects.filter(indexKey__in=simAll.values('x_axis'))
		simClinicalTrials = ClinicalTrial.objects.filter(indexKey__in=simAll.values('x_axis'))
		MeshChart.chart(publications)
		AuthorChart.chart(publications)
		PublicationHistoryChart.chart(publications)

		return render(request, 'searchFunction/userprofile.html', {'profiles' : profiles, 'simAll' : simAll, 'simGrants' : simGrants, 'simAuthors' : simAuthors, 'simClinicalTrials' : simClinicalTrials, 'publications':publications} )


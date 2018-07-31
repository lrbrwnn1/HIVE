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


#Here I want to have the term matched to it's vector, 
#then take the vectors and iterate through all author/grant vectors and find the cos value for each combination 
#How do I take each termVector and extract it, convert to list of floats, do the same for author grant vectors, then find cosine values for each combo, then return Authors/grants with positive values.

def LSI(request):
	if request.method == 'GET':
		LSI_search_query = request.GET.get('search_box', None)
		tl = terms_list.objects.filter(term__icontains=LSI_search_query)
		tv = term_vectors.objects.all()
		termVectorQS = tv.filter(pk__in=tl).values()
		termList = [] #temp list to hold term lists until float conversion is done.
		agvList = []
		agvResults = {}
		for vectorList in termVectorQS:
			termList.append(list(map(float, vectorList['termVector'].split())))

		agv = author_grant_vectors.objects.values()
		for t in agv:
			agvList.append(list(map(float, t['grantvector'].split())))
		
		for x in termList:
			count = 0
			for y in agvList:
				count+=1
				if cosine_similarity([x],[y])[0][0]>.1:
					agvResults[count] = cosine_similarity([x],[y])[0][0]
		
		g = agvResults.keys()
		termVecto = author_grant_vectors.objects.filter(id__in=g)
		termVectors = termVecto.values('item')
		Authors = termVecto.filter(item__contains='Author')
		authorsFiltered = termVecto.filter(item__contains='Author').values_list('item')
		Grants = termVecto.filter(item__contains='Grant')
		profiles = Investigator.objects.filter(investigator_tag__in=authorsFiltered).values()
			







		return render(request, 'searchFunction/LSI.html',{'Authors' :  Authors, 'Grants' :  Grants, 'profiles' : profiles})

def profile(request):
	if request.method == 'GET':
		profiles = Investigator.objects.all()
		return render(request, 'searchFunction/profile.html',{'profiles' : profiles})




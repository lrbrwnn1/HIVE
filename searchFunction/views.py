from django.shortcuts import render
from .models import Investigator
from .models import Grant
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView

def index(request):
    return render(request, 'searchFunction/index.html',{})

def results(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		grants = Grant.objects.filter(title__icontains=search_query).values('title', 'expiryDate', "guidelink")

		return render(request, 'searchFunction/results.html',{'grants': grants})





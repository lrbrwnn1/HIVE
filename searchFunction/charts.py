import pygal
from collections import Counter
from .models import Investigator
from .models import Publication
from .models import Grant
from .models import terms_list
from .models import author2citation
from .models import term_vectors
from .models import author_grant_vectors
from .models import grant_documents
from .models import authors_grants_pairwise_cosine_similarity_matrix
from django.http import HttpResponse
from pygal.style import BlueStyle
import re

class MeshChart():
	def chart(publications):
		pubs = publications.values('meshHeadings')
		meshHeadList = []
		for meshes in pubs:
			meshHeadList.append(list(map(str, meshes['meshHeadings'].split())))
		counts = {}
		for p in meshHeadList:
			for i in p:
				i = ' '.join([w for w in i.split() if len(w)>2])
				#need to add something here to strip out all non-alphanumeric chars 
				if i in counts:
					counts[i]+=1
				else:
					counts[i]=1
		x = dict(Counter(counts).most_common(10))

		bar_chart = pygal.HorizontalBar(title=u'Top Research Interests by MeSH Headings', style=BlueStyle, legend_at_bottom=True)               
		for y in x:
			bar_chart.add(y, x[y])
		bar_chart.render_to_file('./searchFunction/static/mesh_chart.svg')

class AuthorChart():
	def chart(publications):
		pubs = publications.values('authors')

		g=[]
		for y in pubs:
		  text = re.sub('[^A-Za-z, ]', '', str(y['authors'].split(", ")))
		  g.append(text)

		counts=[]
		for i in g:
		  i = i.split(", ")
		  counts.append(i)
		thingy = {}
		for a in counts:
		  for b in a:
		    if b in thingy:
		      thingy[b]+=1
		    else:
		      thingy[b]=1
		x = dict(Counter(thingy).most_common(6)[1:])

		bar_chart = pygal.Pie(inner_radius=.4, title=u'Top Co-authors', style=BlueStyle, legend_at_bottom=True)               
		for y in x:
			bar_chart.add(y, x[y])
		bar_chart.render_to_file('./searchFunction/static/author_chart.svg')
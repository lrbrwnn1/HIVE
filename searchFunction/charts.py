from __future__ import unicode_literals
import pygal
from collections import Counter
from .models import Investigator
from .models import Publication
from django.http import HttpResponse
from pygal.style import BlueStyle
import re

class MeshChart():
	@staticmethod
	def chart(publications):
		pubs = publications.values('meshHeadings')
		#Data Generation and Formatting
		g=[]
		for y in pubs:
		  text = re.sub('[^A-Za-z, ]', '', str(y['meshHeadings'].split(", ")))
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
		x = dict(Counter(thingy).most_common(10))
		#Graph Creation
		bar_chart = pygal.HorizontalBar(
			legend_at_bottom=True,
			title=u'Top Research Interests by MeSH Headings', 
			x_title='Frequency',
			y_title='MeSH Heading',
			print_values=True,
			print_labels=True,
			style=BlueStyle(
            value_font_family='googlefont:Raleway',
	        value_font_size=30,
	        value_colors=('white',)))               
		for y in x:
			bar_chart.add(y, x[y])
		bar_chart.render_to_file('./searchFunction/static/mesh_chart.svg')

class AuthorChart():
	@staticmethod
	def chart(publications):
		pubs = publications.values('authors')
		#Data Generation and Formatting
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
		x = dict(Counter(thingy).most_common(6)[1:]) #The "[1:]" list slice here is because the most common researchers will always be themselves, so we remove the self-reference.
		#Graph Creation
		bar_chart = pygal.HorizontalBar(
			title=u'Top Co-authors',			
			x_title='Number of papers co-authored',
			y_title='Co-author',
			print_values=True,
			print_labels=True,
			style=BlueStyle(
            value_font_family='googlefont:Raleway',
	        value_font_size=30,
	        value_colors=('white',)))              
		for y in x:
			bar_chart.add(y, x[y])
		bar_chart.render_to_file('./searchFunction/static/author_chart.svg')

class PublicationHistoryChart():
	@staticmethod
	def chart(publications):
		pubs = publications.values('datePublished')
		#Data Generation and Formatting
		g=[]
		y=[]
		for y in pubs:
		  text = (y['datePublished'][:4])
		  g.append(text)

		x = Counter()
		for word in g:
			x[word] +=1

		result= dict(x)
		#Graph Creation
		line_chart = pygal.Bar(

			inner_radius=.4, 
			title=u'Publication History',			
			x_title='Year',
			y_title='Number of papers',
			print_values=True,
			print_labels=True,
			style=BlueStyle(
            value_font_family='googlefont:Raleway',
	        value_font_size=30,
	        value_colors=('white',)))    
		for x in result:
			line_chart.add(x , result[x])
		line_chart.render_to_file('./searchFunction/static/pubHistory_chart.svg')
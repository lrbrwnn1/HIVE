from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

#This file defines the database structure for the project (the db name is "hive" if you're looking for it)
#Don't touch anything here unless you know what you're doing and have a specific reason for changing it.
#As always, make sure to backup the db before making any major changes. 


class Investigator(models.Model):
	#Many fields are null here as our information on faculty at Oakland is incomplete for now.
	#The uncommented fields are the ones we have full info on for all members.

	indexKey = models.IntegerField(db_index=True, default=0) 
	fullName = models.TextField(default=' ')
	fName = models.TextField(default=' ')
	#MI = models.TextField(default=' ')
	lName = models.TextField(default=' ')
	#department = models.TextField(default=' ')
	#position = models.TextField(default=' ')
	email = models.EmailField(default=' ')
	location = models.TextField(default=' ')
	#country = models.TextField(default=' ')
	#office = models.CharField(max_length=50,default=' ')
	affiliation = models.TextField(default=' ')
	#phone = models.CharField(max_length=25,default=' ')
	investigator_tag = models.TextField(default=' ')

class Grant(models.Model):
	indexKey = models.IntegerField(db_index=True, default=0)
	grantID = models.TextField(default='')
	guidelink = models.URLField(default='')
	title = models.TextField(default='')
	grantText = models.TextField(default='')

class ClinicalTrial(models.Model):
	indexKey = models.IntegerField(db_index=True, default=0)
	ctID = models.TextField(default='')
	title = models.TextField(default='')
	guidelink = models.URLField(default='')
	status = models.TextField(default='')
	conditions = models.TextField(default='')
	interventions = models.TextField(default='')
	locations = models.TextField(default='')

class Publication(models.Model):
	pmid = models.TextField(default='')
	title = models.TextField(default='')
	abstract = models.TextField(default='')
	affiliation = models.TextField(default='')
	authors = models.TextField(default='')
	source = models.TextField(default='')
	datePublished = models.TextField(default='')
	meshHeadings = models.TextField(default='')
	investigator_tag = models.TextField(default='')

class terms_list(models.Model):
	term = models.TextField(default='')
	termVector = ArrayField(models.FloatField())

class items_list(models.Model):
	indexKey = models.IntegerField(db_index=True, default=0)
	item = models.TextField(default='')
	itemVector = ArrayField(models.FloatField())

class similarity_matrix(models.Model):
	y_axis = models.IntegerField(default=0)
	x_axis = models.IntegerField(default=0)
	cosine_score = models.DecimalField(max_digits=10, decimal_places=10)



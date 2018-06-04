from django.db import models
from django.contrib.auth.models import User


class Investigator(models.Model):
    investigator_id = models.IntegerField(default=0)
    department = models.TextField(default='')
    email = models.EmailField(default='')
    name = models.TextField(default='')
    phone = models.CharField(max_length=25,default='')
    picture = models.ImageField(blank=True, null=True)
    city = models.TextField(default='')
    state = models.TextField(default='')
    country = models.TextField(default='')
    institution = models.TextField(default='')
    office = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.lname

class Grant(models.Model):
    docNum = models.CharField(max_length=30,default='')
    title = models.TextField(default='')
    agency = models.CharField(max_length=30, default='')
    guidelink = models.URLField(default='')
    openDate = models.DateField(blank=True, null=True)
    expiryDate = models.DateField(blank=True, null=True)
    parentFOA = models.CharField(max_length=10, default='')


    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.TextField(default='')
    medline = models.TextField(default='')
    guidelink = models.URLField(default='')

    def __str__(self):
        return self.title



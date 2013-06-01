from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Problem(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	creation_date = models.DateTimeField(auto_add_now=True)

	def __unicode__(self):
		return "%s" % self.title


class Solution(models.Model):
	description = models.TextField()
	creation_date = models.DateTimeField(auto_add_now=True)
	problem = models.ForeignKey(Problem)

	def __unicode__(self):
		return "%s" % self.description[:25]

class Skill(models.Model):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return "%s" % self.title


class MyUser(AbstractBaseUser):
	skills = models.ManyToManyField(Skill)



	def __unicode__(self):
		return "%s" % self.description[:25]


class Project(models.Model):
	title = models.CharField(max_length=100)
	creation_date = models.DateTimeField(auto_add_now=True)
	description = models.TextField()
	skill = models.ManyToManyField(Skill)
	altitude = models.DecimalField()
	latitude = models.DecimalField()
	longitude = models.DecimalField()
	solution = models.ForeignKey(Solution)


	def __unicode__(self):
		return "%s" % self.title

 


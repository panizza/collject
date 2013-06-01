from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title


class Solution(models.Model):
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    problem = models.ForeignKey(Problem)

    def __unicode__(self):
        return "%s" % self.description[:25]

class Skill(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    image = models.ImageField(upload_to="images/user/",null=True)
    skills = models.ManyToManyField(Skill)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return "%s" % self.description[:25]


class Project(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    skill = models.ManyToManyField(Skill)
    latitude = models.FloatField()
    longitude = models.FloatField()
    solution = models.ForeignKey(Solution)


    def __unicode__(self):
        return "%s" % self.title

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)


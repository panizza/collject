from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from api.helpers import get_city_names

class Problem(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    follower = models.ManyToManyField(User, related_name="problemfollower", default=[],blank=True)

    class Meta:
        get_latest_by = "creation_date"

    def __unicode__(self):
        return "%s" % self.title


class Solution(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    problem = models.ForeignKey(Problem)
    follower = models.ManyToManyField(User, related_name="solutionfollower", default=[], blank=True)

    def __unicode__(self):
        return "%s" % self.description[:25]

class Skill(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    image = models.ImageField(upload_to="images/user/", null=True)
    skills = models.ManyToManyField(Skill)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def get_image_url(self):
        return self.image if self.image else ""


    def __unicode__(self):
        return "%s" % self.user.username


class Project(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    skill = models.ManyToManyField(Skill)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    solution = models.ForeignKey(Solution)
    user = models.ForeignKey(User)
    follower = models.ManyToManyField(User, related_name="projectfollower", default=[], blank=True)
    city =models.TextField(null=True,blank=True)

    def save(self):
        self.city = get_city_names(self.latitude,self.longitude)
        super(Project, self).save()

    def __unicode__(self):
        return "%s" % self.title


#@receiver(post_save, sender=Solution)
#def post_save_do_stuff(sender, **kwargs):
#    """ Calls the do_stuff function on the saved instance if it was
#        just created
#    """
#    if kwargs['created']:
#        kwargs['instance']._do_stuff()


@receiver(post_save, sender=User)
def post_save_user_stuff(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        profile, created = UserProfile.objects.get_or_create(user=user)

from django.shortcuts import render, get_object_or_404
from basetyzer.models import Problem, Project, Solution
from django.db.models import Count
from .helpers import MyJsonEncoder
import json 

def index(request):
    return render(request, "app/index.html")




"""lista di tutti i problemi ordinata per follower
lista di tutti i progetti ordinata per follower
lista di tutte le soluzioni ordinata per +1

dato un utente
 - lista di tutti i problemi ordinata per data last update (last_update generato da ultima modifica a una soluzione di quel problema)
 - lista di tutti i progetti che followo o che ho creato


progetti -> lista di followers
idee -> lista di user che hanno fatto +1
problemi -> lista di follower"""


def list_project(request):
	prjs = Project.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
	print json.dumps(prjs,cls=MyJsonEncoder)


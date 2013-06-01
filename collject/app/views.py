from django.shortcuts import render, get_object_or_404
from basetyzer.models import Problem, Project, Solution
from django.contrib.auth.models import User
from django.db.models import Count,Q
from .helpers import my_json_encoder
import json 

def index(request):
    return render(request, "app/index.html")




"""
l√ista di tutti i problemi ordinata per follower
√lista di tutti i progetti ordinata per follower
√lista di tutte le soluzioni ordinata per +1

dato un utente
 - lista di tutti i problemi ordinata per data last update (last_update generato da ultima modifica a una soluzione di quel problema)
 √ lista di tutti i progetti che followo o che ho creato


√progetti -> lista di followers
√idee -> lista di user che hanno fatto +1
√problemi -> lista di follower
"""


def list_problem(request):
	prbs = Problem.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
	print json.dumps(prbs, default=my_json_encoder)

def list_project(request):
	prjs = Project.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
	print json.dumps(prjs, default=my_json_encoder)

def list_solution(request):
	sols = Solution.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
	print json.dumps(sols, default=my_json_encoder)

def list_updated_problem(request):
	


def list_my_project(request):
	user= get_object_or_404(User, pk=request.user.id)
	prjs = Project.objects.filter(Q(user=user)| Q(follower__in=[user]))
	print json.dumps(prjs,default=my_json_encoder)

def list_follower_of_project(request):
	project = get_object_or_404(Project, pk=request.project.id)
	flws = project.follower.all().values()
	print json.dumps(flws)

def list_follower_of_solution(request):
	sol = get_object_or_404(Solution, pk=request.solution.id)
	flws = sol.follower.all().values()
	print json.dumps(flws)

def list_follower_of_problem(request):
	prob = get_object_or_404(Problem, pk=request.problem.id)
	flws = prob.follower.all().values()
	print json.dumps(flws)


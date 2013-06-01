from django.shortcuts import render, get_object_or_404
from basetyzer.models import Problem, Project, Solution
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ajaxutils.decorators import ajax
from django.db.models import Count, Q
from .helpers import encode_json
import json 

@ajax(require="GET")
def list_problem(request):
    prbs = Problem.objects.annotate(follower_count=Count("follower")).order_by("-follower_count")
    return encode_json(prbs.values('id', 'title', 'description', 'follower_count'))

@ajax(require="GET")
def get_problem_info(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    return encode_json(prob.values())

@ajax(require="GET")
def get_solution_of_problem(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    sols = prob.solution_set.all()
    return encode_json(sols.values('id', 'description'))

@ajax(require="GET")
def list_project(request):
    prjs = Project.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
    json_out = json.loads(encode_json(prjs.values('id', 'title', 'description', 'follower_count', 'creation_date', 'latitude', 'longitude')))
    for obj in json_out:
        obj['img'] = User.objects.get(pk=obj['owner_id']).get_profile().get_image_url()
    return json_out

@ajax(require="GET")
def get_project_info(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return encode_json(project.values())

@ajax(require="GET")
def list_solution(request):
    sols = Solution.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
    return encode_json(prbs.values('id','problem_id','description','follower_count','creation_date'))

@ajax(require="GET")
def get_solution_info(request, solution_id):
    sol = get_object_or_404(Solution, pk=solution_id)
    return encode_json(sol.values())

@login_required
@ajax(require="GET")
def list_my_project(request):
    user= get_object_or_404(User, pk=request.user.id)
    prjs = Project.objects.filter(Q(user=user)| Q(follower__in=[user]))
    return encode_json(prbs.values('id','title','description','follower_count','creation_date'))

@ajax(require="GET")
def list_follower_of_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    flws = project.follower.all()
    return encode_json(flws.values('id','email'))

@ajax(require="GET")
def list_follower_of_solution(request, solution_id):
    sol = get_object_or_404(Solution, pk=solution_id)
    flws = sol.follower.all().values()
    return encode_json(flws.values('id','email'))

@ajax(require="GET")
def list_follower_of_problem(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    flws = prob.follower.all().values()
    return encode_json(flws.values('id','email'))


from django.shortcuts import render, get_object_or_404
from basetyzer.models import Problem, Project, Solution
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ajaxutils.decorators import ajax
from django.db.models import Count, Q
from django.http import QueryDict
from django.forms.models import model_to_dict
from .helpers import encode_json, _my_json_encoder, get_city_names
from django.views.decorators.csrf import csrf_exempt
import json
import requests



@ajax(require="GET")
def list_problem(request):
    prbs = Problem.objects.annotate(follower_count=Count("follower")).order_by("-follower_count")
    return encode_json(prbs.values('id', 'title', 'description', 'follower_count'))


@ajax(require="GET")
def get_problem_info(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    return _my_json_encoder(model_to_dict(prob))


@ajax(require="GET")
def get_solution_of_problem(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    sols = prob.solution_set.all()
    return encode_json(sols.values('id', 'description'))


@ajax(require="GET")
def list_project(request):
    prjs = Project.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
    json_out = encode_json(prjs.values('id', 'title', 'user', 'description', 'follower_count', 'creation_date', 'latitude', 'longitude'))
    for obj in json_out:
        obj['img'] = User.objects.get(pk=obj['user']).get_profile().get_image_url()
    return json_out


@ajax(require="GET")
def get_project_info(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return _my_json_encoder(model_to_dict(project))


@ajax(require="GET")
def list_solution(request):
    sols = Solution.objects.annotate(follower_count=Count("follower")).order_by("-follower_count").values()
    return encode_json(sols.values('id', 'problem_id', 'description', 'follower_count', 'creation_date'))


@ajax(require="GET")
def get_solution_info(request, solution_id):
    sol = get_object_or_404(Solution, pk=solution_id)
    return _my_json_encoder(model_to_dict(sol))


@login_required
@ajax(require="GET")
def list_my_project(request):
    user = get_object_or_404(User, pk=request.user.id)
    prjs = Project.objects.filter(Q(user=user)|Q(follower__in=[user]))
    return encode_json(prjs.values('id', 'title', 'description', 'follower_count', 'creation_date'))


@ajax(require="GET")
def list_follower_of_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    flws = project.follower.all()
    return encode_json(flws.values('id', 'email'))


@ajax(require="GET")
def list_follower_of_solution(request, solution_id):
    sol = get_object_or_404(Solution, pk=solution_id)
    flws = sol.follower.all().values()
    return encode_json(flws.values('id', 'email'))


@ajax(require="GET")
def list_follower_of_problem(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    flws = prob.follower.all().values()
    return encode_json(flws.values('id', 'email'))


@ajax(require="POST")
@csrf_exempt
def search_project_from_skill(request):
    print request.POST
    skills = ['carpentiere', 'JAVA']
    return encode_json(Project.objects.filter(skill__title__in=skills).values())

@ajax(require="POST")
@csrf_exempt
def search_project_from_position(request):
    print request.POST
    pos = QueryDict(request.POST).dict()
    city= get_city_names(pos['lat'],pos['lng'])
    return encode_json(Project.objects.filter(city=city));

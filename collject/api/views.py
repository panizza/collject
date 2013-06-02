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
import operator


@ajax(require="GET")
def list_problem(request):
    prbs = Problem.objects.annotate(follower_count=Count("follower")).order_by("-follower_count")
    json_out = encode_json(prbs.values('id', 'title', 'description', 'follower_count', 'owner', 'hashtag'))
    for obj in json_out:
        user = User.objects.get(pk=obj['owner'])
        obj['owner'] = model_to_dict(user, fields=['username', 'id', 'email'])
        obj['owner']['img'] = user.get_profile().get_image_data_uri()
        obj['owner']['skills'] = encode_json(user.get_profile().skills.values())
    return json_out


@ajax(require="GET")
def get_problem_info(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    return _my_json_encoder(model_to_dict(prob))


@ajax(require="POST")
@csrf_exempt
def search_problem_from_hashtag(request):
    json_in =json.loads(json.dumps(request.POST))
    print json_in
    skills = json_in['hashtag'].split(',')
    return encode_json(Problem.objects.filter(reduce(operator.or_, (Q(hashtag=x) for x in skills))).values())


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
        user = User.objects.get(pk=obj['user'])
        obj['user'] = model_to_dict(user, fields=['username', 'id', 'email'])
        obj['user']['img'] = user.get_profile().get_image_data_uri()
        obj['user']['skills'] = encode_json(user.get_profile().skills.values())
    return json_out


@ajax(require="GET")
def get_project_info(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return _my_json_encoder(model_to_dict(project))


@ajax(require="GET")
def list_solution(request):
    sols = Solution.objects.annotate(follower_count=Count("follower")).order_by("-follower_count")
    json_out = encode_json(sols.values('id', 'problem_id', 'user', 'description', 'follower_count', 'creation_date'))
    for obj in json_out:
        user = User.objects.get(pk=obj['user'])
        print user
        obj['user'] = model_to_dict(user, fields=['username', 'id', 'email'])
        obj['user']['img'] = user.get_profile().get_image_data_uri()
        obj['user']['skills'] = encode_json(user.get_profile().skills.values())
    return json_out


@ajax(require="GET")
def get_solution_info(request, solution_id):
    sol = get_object_or_404(Solution, pk=solution_id)
    return _my_json_encoder(model_to_dict(sol))


@login_required
@ajax(require="GET")
def list_my_project(request):
    user = get_object_or_404(User, pk=request.user.id)
    prjs = Project.objects.filter(Q(user=user) | Q(follower__in=[user]))
    json_out = encode_json(prjs.values('id', 'title', 'user', 'description', 'follower_count', 'creation_date', 'latitude', 'longitude'))
    for obj in json_out:
        user = User.objects.get(pk=obj['user'])
        obj['user'] = model_to_dict(user, fields=['username', 'id', 'email'])
        obj['user']['img'] = user.get_profile().get_image_data_uri()
        obj['user']['skills'] = encode_json(user.get_profile().skills.values())
    return json_out


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
    json_in =json.loads(json.dumps(request.POST))
    skills = json_in['skill']
    print skills
    return encode_json(Project.objects.filter(skill__title__in=skills).values())


@ajax(require="POST")
@csrf_exempt
def search_project_from_position(request):
    lat = request.POST.get('lat', None)
    lon = request.POST.get('lng', None)
    if lat and lon:
        city = get_city_names(lat, lon)
        return encode_json(Project.objects.filter(city=city).values())
    else:
        return encode_json([])


@ajax(require="POST")
@csrf_exempt
def search_problem_from_position(request):
    city = request.POST.get('city', None)
    return encode_json(Problem.objects.filter(city=city).values()) if city else encode_json([])

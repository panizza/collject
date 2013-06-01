from django.conf.urls import patterns, url, include


urlpatterns = patterns('api.views',
    url(r'^problem/list/$', 'problem_list', name='problem_list'),
    url(r'^problem/(?P<problem_id>\d+)/info/$', 'get_problem_info', name='get_problem_info'),
    url(r'^problem/(?P<problem_id>\d+)/solutions/$', 'get_solution_of_problem', name='get_solution_of_problem'),
)


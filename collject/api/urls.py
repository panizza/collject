from django.conf.urls import patterns, url, include


urlpatterns = patterns('api.views',
                       url(r'^problem/list/$', 'list_problem', name='list_problem'),
                       url(r'^problem/(?P<problem_id>\d+)/info/$', 'get_problem_info', name='get_problem_info'),
                       url(r'^problem/(?P<problem_id>\d+)/solution/$', 'get_solution_of_problem', name='get_solution_of_problem'),
                       url(r'^problem/(?P<problem_id>\d+)/follower/$', 'list_follower_of_problem', name='list_follower_of_problem'),

                       url(r'^project/list/$', 'list_project', name='list_project'),
                       url(r'^project/(?P<project_id>\d+)/info/$', 'get_project_info', name='get_project_info'),
                       url(r'^project/(?P<project_id>\d+)/follower/$', 'list_follower_of_project', name='list_follower_of_project'),
                       url(r'^project/(?P<project_id>\d+)/search/$', 'list_follower_of_project', name='list_follower_of_project'),

                       url(r'^solution/list/$', 'list_solution', name='list_solution'),
                       url(r'^solution/(?P<solution_id>\d+)/info/$', 'get_solution_info', name='get_solution_info'),
                       url(r'^solution/(?P<solution_id>\d+)/follower/$', 'list_follower_of_solution', name='list_follower_of_solution'),
)


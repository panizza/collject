from django.contrib import admin
from basetyzer.models import Project, Problem, Solution

#add MyGroup to /admin
admin.site.register(Project)
admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(Skill)


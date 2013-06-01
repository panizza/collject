from django.shortcuts import render, get_object_or_404
from ajaxutils.decorators import ajax

def index(request):
    return render(request, "app/index.html")
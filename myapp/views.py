from django.shortcuts import render
from .models import *
from .utils import *
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
def hello(request):
    return HttpResponse('Hello world !')
def my_view(request,id):
    try:
        obj = Reporter.objects.get(id=id)
    except Reporter.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    html =f"<html><body><h1>Reporter is {obj} </h1></body></html>"
    return HttpResponse(html)




def index2(request):
    return HttpResponse('hello from inx 2!')

def index3(request):
    return HttpResponse('hello from inx 3!')

from django.http import HttpResponse, HttpResponseNotFound


# def my_view(request):
#     foo =False
#     if foo:
#         return HttpResponseNotFound("<h1>Page not found</h1>")
#     else:
#         return HttpResponse("<h1>Page was found</h1>")

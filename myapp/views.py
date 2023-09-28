from django.shortcuts import render
from .models import *
from .utils import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse,Http404
from .forms import *
def hello(request):
    return HttpResponse('Hello world !')

def funct(request):
    html = f"<html><body><h1>hello world i</h1></body></html>"
    return HttpResponse(html)


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = 'gs6506223@gmail.com' 

            send_mail(subject, message, sender, [recipient])

            return redirect('email_sent')  
    else:
        form = EmailForm()

    return render(request, 'myapp/eamil.html', {'form': form})

def sucess_email(request):
    return render(request,'myapp/success.html')

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

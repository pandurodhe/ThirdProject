from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2> Good morning  user...!! have  a  nice day.....</h2><hr/>");
def f2(request):
    return HttpResponse("<h2> Good afternoon  user...!! how was the day.....</h2><hr/>");
def f3(request):
    return HttpResponse("<h2> Good evening  user...!! today is good.....</h2><hr/>");
            
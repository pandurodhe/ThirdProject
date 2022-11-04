from django.shortcuts import render

# Create your views here.
def display(request): #view-function
    print("welcome/ url is requested & display() is executed")
    ss = "<center><h2 style='color:blue;'>Hello User, Welcome to django first-project first-app</h2 >  <hr color='red' width='80%' size='7'/></center>";
    return HttpResponse(ss); 
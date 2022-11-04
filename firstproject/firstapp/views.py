from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
    print("welcome/ url is requested & display() is executed")
    ss = "<center><h2 style='color:blue;'>Hello User, Welcome to django first-project first-app</h2 >  <hr color='red' width='80%' size='7'/></center>";
    return HttpResponse(ss); 
    

    
    
def  show(request):
    ss='''
    <html>
        <head>
        <title>haiii welcome to the webpage</title>
        h1{
            color:red;
          }
        h2{
            color:pink;
          }
        h3{
            color:yello;
          }            
        /head>
        <body>
        <center>
            <h1>hello user...!!!!!!!</h1>
            <hr color='red' width='70'/>
            <h2>have a nice day....!!!!<h2/>
            <hr color='blue width='80'/>
            <h3>may god bless you.....!!!!!!<h3/>
            <hr color='pink' width='50'/>
            /center>
            /body>
            </html>
        </center>    
        ''';
    return HttpResponse(ss);   
    
import time;
def senddatetime(request):
    print("dtime/ url is required & senddatetime() is executed");
    ct= time.ctime();
    print("Client Request Date &time on server ::",ct);
    ss='''
    <html>
        <head>
            <title>Date-time Webpage</title>
            <style>
            h1{   
                      
		        color:blue;
              }
		    h2{
                color:red;
                			
              }
            h3{ 
            
               color:green;   
              }
            h1,h2,h3{ 
                     background:pink; width:70%;
                    }
            h2,h4,h6{
                     background:yello; width:60%;
                    }                  
                   
                </style>          
		<body>
		<center>
                  h1{
                        color:Blue;
                    }
                  h2{
                        color:red;
                    
                    }
                  h3{
                       color:green;   
                    }
                  h4{ 
                       color:pink;
                    }
                  h5{
                       color:yellow;
                     }
                  h6{
                       color:black;
                    }  
                </style> 			
                <h1>welcome to Django-user.......!!!!</h1>
                <hr color='green' width="95%"/>		
                <h2>Server-date & Time  :: </h2>
                <hr color='yello' width='60%'/>		
                <h3>''',ct,'''</h3>        
                </body>
        </head>
	    </center>        
    </html>            
      '''
    return HttpResponse(ss);
def demo(request):
    print("multiple-Request-URLS same response");
    htmldata='''<center><h1>Welcome demo user...!!</h1><hr/>
    <h2>this is same-output for different-multiple-Request-URLS</h2><hr/>
    <h3> have a great day.....</h3>
    </center>''';
    return HttpResponse(htmldata);
def homepage(request):
    htmldata='''<center>
    <h1>WELCOME TO DEFAULT HOME PAGE......!!!</h1></hr>
    <h2>YOUR REQUEST PAGE IS NOT FOUND.....!!!<h2></hr>
    <h3>PLEASE TRY OTHER URL AND OTHER LINK...!!!<h3></hr>
    </center>'''
    return HttpResponse(htmldata);
    















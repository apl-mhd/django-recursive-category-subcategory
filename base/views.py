from queue import Empty
from django.shortcuts import render
from . models import *

# Create your views here.

#global a 

def index(request):

    catagories = Category.objects.filter(parent = NULL)
    htmltag = "<ul>"

    def rec(i, x): 
        child = Category.objects.filter(parent = i )
        if(len(child) != 0):
            x +="<ul>"
            for i in child:
                x +="<li>"+ str(i)
                x =rec(i.id, x)
            
            x +="</ul>"
        x += "</li>"
        return x

    
    for j in catagories:
        htmltag += "<li>"+ str(j) 
        print(j)
        htmltag = rec(j.id, htmltag)

    htmltag += "</ul>"

    #print(htmltag)

    context = {'htmltag': htmltag }

    return render(request, "base/index.html", context)



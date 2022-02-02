from queue import Empty
from django.shortcuts import render
from . models import *

# Create your views here.

#global a 

def index(request):

    catagories = Category.objects.filter(parent = NULL)
    htmltag = "<ul>"

    def recur(id, x): 
        child = Category.objects.filter(parent = id )
        if(len(child) != 0):
            x += "<ul>"
            for j in child:
                x += "<li>"+ j.name
                x = recur(j.id, x)
            
            x +="</ul>"
        x += "</li>"
        return x

    
    for cat in catagories:
        htmltag += "<li>"+ cat.name
        #print(cat)
        htmltag = recur(cat.id, htmltag)

    htmltag += "</ul>"

    #print(htmltag)

    context = {'htmltag': htmltag }

    return render(request, "base/index.html", context)



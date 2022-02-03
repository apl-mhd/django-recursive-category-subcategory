from queue import Empty
from django.shortcuts import render
from . models import *

# Create your views here.

#global a 

def index(request):

    
    c = str(1)
    a = '<a id="'+c+'" href="">'
    print(a)

    #allChild = Category.objects.filter( id not parent)
    catagories = Category.objects.filter(parent = NULL)
    htmltag = '<ul>'

    def recur(id, x): 
        child = Category.objects.filter(parent = id )
        if(len(child) != 0):
            x += '<ul>'
            for j in child:
                id = str(j.id)
                x += '<li> <a id="'+id +'" href="#">'+ j.name + '</a>'
                x = recur(j.id, x)
            
            x +='</ul>'
        x += '</li>'
        return x

    
    for cat in catagories:
        id = str(cat.id)
        #x += '<li id="'+id+'">'+ j.name
        htmltag += '<li> <a id="'+id +'"  href="#">'+ cat.name + '</a>'
        #print(cat)
        htmltag = recur(cat.id, htmltag)

    htmltag += '</ul>'

    context = {'htmltag': htmltag }

    return render(request, "base/index.html", context)



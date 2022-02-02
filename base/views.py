from queue import Empty
from django.shortcuts import render
from . models import *

# Create your views here.

#global a 

def index(request):

    genres = Genre.objects.all()
    gen = list(Genre.objects.values())
    tags = Tag.objects.all()
    category = Genre.objects.filter(parent=None)

    htmltag = "<ul>"
   

    catagories = Category.objects.filter(parent = NULL)
    #a = "<ul> <li>" + str(catagories[0]) + "</ul></li>"
    #print(Category.objects.get(parent=catagories.id ))
    

    def rec(i, x): 
        child = Category.objects.filter(parent = i )
        if(len(child) != 0):
            x +="<ul>"
            for i in child:
                x +="<li>"+ str(i)
                x =rec(i.id, x)
            
            x +="</ul>"


        #  x +="<ul>"
        #  for i in child:
        #      x +="<li>"+ str(i) 
        #      x = rec(i.id, x)
        # a +="<li>" 
        # for i in child:
        #  a +="<li>"+ str(i) +"</li>"
        #  print(i)
        #  rec(i.id, a)
        x += "</li>"
        return x

    
    for j in catagories:
        htmltag += "<li>"+ str(j) 
        print(j)
        htmltag = rec(j.id, htmltag)

    htmltag += "</ul>"

    print(htmltag)




    context = {'genres': genres, 'gen':gen, 'tags':tags, 'category': category, 'catagories':catagories ,'htmltag': htmltag }

    return render(request, "base/index.html", context)



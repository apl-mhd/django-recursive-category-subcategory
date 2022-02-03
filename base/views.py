
from queue import Empty
from django.http import JsonResponse
from django.shortcuts import render
from . models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#global a 

def htmlOutput():

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

    categories = Category.objects.filter(parent = NULL)

    for cat in categories:
        id = str(cat.id)
        htmltag += '<li> <a id="'+id +'"  href="#">'+ cat.name + '</a>'
        htmltag = recur(cat.id, htmltag)

    htmltag += '</ul>'
    return htmltag




def index(request):


    #allChild = Category.objects.filter( id not parent)
    #catagories = Category.objects.filter(parent = NULL)
    # htmltag = '<ul>'

    # def recur(id, x): 
    #     child = Category.objects.filter(parent = id )
    #     if(len(child) != 0):
    #         x += '<ul>'
    #         for j in child:
    #             id = str(j.id)
    #             x += '<li> <a id="'+id +'" href="#">'+ j.name + '</a>'
    #             x = recur(j.id, x)
            
    #         x +='</ul>'
    #     x += '</li>'
    #     return x

    
    # for cat in catagories:
    #     id = str(cat.id)
    #     htmltag += '<li> <a id="'+id +'"  href="#">'+ cat.name + '</a>'
    #     htmltag = recur(cat.id, htmltag)

    # htmltag += '</ul>'
    htmltag = htmlOutput()

    context = {'htmltag': htmltag }

    return render(request, "base/index.html", context)

@csrf_exempt
def saveCategory(request):
    print(request.POST)
    #{'catName': ['a'], 'catId': ['5']}>
    if request.method == 'POST':
        catName = request.POST['catName']
        catId = request.POST['catId']

        category = Category(name=catName, parent=catId)
        category.save()

    htmltag = htmlOutput()


    return JsonResponse({'status': 1, 'htmltag':htmltag})



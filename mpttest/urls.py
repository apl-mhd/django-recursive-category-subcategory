
from unicodedata import name
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('save-category/', views.saveCategory, name='save-category')
]

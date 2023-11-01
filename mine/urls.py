from django.contrib import admin
from django.urls import path
from mine import views
urlpatterns = [
 path ('',views.index, name='home') ,
#  path ('about',views.about, name='about') ,
#  path ('skills',views.skills, name='skills') ,
#  path ('projects',views.projects, name='projects') ,
#  path ('contact',views.contact, name='contact') 



]
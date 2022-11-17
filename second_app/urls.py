from django.contrib import admin
from django.urls import path,re_path,include
from second_app import views

urlpatterns = [
    path('',views.users,name='show_user'),


    
]
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:lion_id>' , views.detail , name = "detail"),
    path('write/', views.write, name='write'),
    path('create/', views.create, name="create"),
]
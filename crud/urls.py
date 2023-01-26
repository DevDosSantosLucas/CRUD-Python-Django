from django.contrib import admin
from django.urls import path,include
from .views import  read ,create , edit, update, delete

urlpatterns = [
    path('', read ),
    path('create/', create, name = "create"),
    path('edit/<int:id>', edit, name="edit"), 
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]

from django.urls import path

from . import views

app_name='eshop_Searchapp'

urlpatterns = [
   path('', views.SearchResults, name='SearchResults'),
]

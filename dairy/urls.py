from django.urls import path
from .views import index,DoneView
urlpatterns =[
    path('',DoneView.as_view(),name='index'),
    ]
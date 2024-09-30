from django.urls import path
 
from .views import homePageView, listView
 
urlpatterns = [
    path('', homePageView, name='home'),
    path('list/', listView, name='list'),
] 

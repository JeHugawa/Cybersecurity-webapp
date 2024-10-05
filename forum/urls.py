from django.urls import path

from .views import homePageView, postsView, privatePostsView, profileView

app_name = 'forum'
urlpatterns = [
    path('', homePageView, name='home'),
    path('<username>/', profileView, name='profile'),
#    path('<username>/posts', postsView, name='posts'),
#    path('<username>/private-posts', privatePostsView, name='Private posts'),
]

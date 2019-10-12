from django.conf.urls import url, include
from . import views
from rest_framework import routers 


urlpatterns = [
    url(r'^api/v1/movies/(?P<pk>[0-9]+)$', # Url to get update or delete a movie
        views.get_delete_update_movie.as_view(),
        name='get_delete_update_movie'
    ),
    url('api/v1/movies/', # urls list all and create new one
        views.get_post_movies.as_view(),
        name='get_post_movies'
    ),
    url('get/movies/', 
        views.get_post_movies.as_view(),
        name='get_movies'
    ),
]

from django.urls import path, include 

from rest_framework.routers import DefaultRouter

from .api.movies.base import MoviesApiView


cinema_router = DefaultRouter() 

cinema_router.register(r'movies', MoviesApiView, basename='movies')



urlpatterns = [ 

    path('', include(cinema_router.urls))

]
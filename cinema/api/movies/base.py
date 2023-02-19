
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from cinema.models.movies.model import Movies
from cinema.serializers.movies.movie_serializer import MoviesSerializer


class MoviesApiPagination(PageNumberPagination): 

    max_page_size = 100
    page_size = 50
    page_size_query_param = 'page_size'

class MoviesApiView(ModelViewSet): 

    queryset = Movies.objects.all() 
    serializer_class = MoviesSerializer
    permission_classes = (AllowAny, )
    pagination_class = MoviesApiPagination



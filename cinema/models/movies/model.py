
from django.db import models 
from django.utils.translation import gettext_lazy as _

from cinema.models.movies.manager import MovieManager

class Movies(models.Model): 

    show_id = models.BigAutoField(primary_key=True, unique=True)
    show_type = models.CharField(max_length=24, null=False, blank=False)
    show_title = models.CharField(max_length=64, null=False, blank=False)
    director = models.CharField(max_length=64, null=False, blank=False)
    cast = models.CharField(max_length=512, null=False, blank=False)
    country = models.CharField(max_length=36, null=False, blank=False)
    date_added = models.CharField(max_length=24, null=False, blank=False)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=10, null=False, blank=False)
    duration = models.CharField(max_length=24, null=False, blank=False)

    objects = MovieManager() 

    def __str__(self): 
        f'{self.show_title}'

    


    
        

    



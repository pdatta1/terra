

from django.db import models 
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _ 


class MovieManager(models.Manager): 


    def filter_shows_or_movies(self, show_type): 
        return self.filter(show_type=show_type)

    def filter_by_directory(self, director_name): 
        return self.filter(director=director_name)

    def filter_by_country(self, country): 
        return self.filter(country=country)

    def filter_by_date_added(self, date_added): 
        return self.filter(date_added=date_added)

    def filter_by_released_year(self, released_year): 
        return self.filter(released_year=released_year)


    def get_show(self, show_title): 
        
        try: 
            show = self.get(show_title=show_title)
            return show 
        except ObjectDoesNotExist:
            raise KeyError(_('Show/Movie is not found!'))


    

        

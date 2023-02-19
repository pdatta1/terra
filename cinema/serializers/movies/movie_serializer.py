

from rest_framework import serializers


from cinema.models.movies.model import Movies



class MoviesSerializer(serializers.ModelSerializer): 


    show_id = serializers.ReadOnlyField() 
    show_type = serializers.CharField(min_length=2, max_length=24, allow_blank=False)
    show_title = serializers.CharField(min_length=2, max_length=64, allow_blank=False)
    director = serializers.CharField(min_length=5, max_length=64, allow_blank=False)
    cast = serializers.CharField(min_length=5, max_length=512, allow_blank=False)
    country = serializers.CharField(min_length=3, max_length=36, allow_blank=False)
    date_added = serializers.CharField(min_length=5, max_length=24, allow_blank=False)
    release_year = serializers.IntegerField() 
    rating = serializers.CharField(min_length=2, max_length=25, allow_blank=False)
    duration = serializers.CharField(min_length=3, max_length=24, allow_blank=False)


    class Meta: 

        model = Movies
        fields = '__all__'
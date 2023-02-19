
import pandas as pd
import numpy as np 
import os 
import pathlib
import cinema
import json

from progress.bar import Bar 

from django.utils.translation import gettext_lazy as _
from django.db import transaction


from cinema.models.movies.model import Movies 


SUPPORT_FILES = { 
    'json': '.json',
    'csv': '.csv'
}


class PopulationUtils(object): 

    def __init__(self, module, cleanup=False):

        self.file_module = os.path.dirname(module.__file__)
        if cleanup: 
            self.clear_database() 


    def read_file(self, file_path): 

        _dataframe = None 
        _directory = os.path.join(self.file_module, file_path)
        _valid_extensions = [extension for extension in SUPPORT_FILES.values()]

        print(f'Valid Extenstion DEBUG #1: {_valid_extensions}')
        file_extension = pathlib.Path(_directory).suffix

        print(f'POPULATE DEBUG #2: {file_extension}')


        if not os.path.exists(_directory): 
            raise ValueError(_('File path not found'))

        if file_extension not in _valid_extensions: 
            raise ValueError(_(f'{file_extension} is not a valid extension'))


        if file_extension == SUPPORT_FILES['json']: 
            _dataframe = pd.read_json(_directory)

        if file_extension == SUPPORT_FILES['csv']: 
            _dataframe = pd.read_csv(_directory)


        return _dataframe



    def save_to_model_csv(self, directory): 

        file_dir = os.path.join(self.file_module, directory)
        bulk_data = []  

        df = self.read_file(file_dir) 
        data = df.to_dict('show_id') 
        data_length = len(data['show_id'])

        progress = Bar('Upload Data to Model', max=data_length)

        for id in range(data_length): 

            movie_model =  Movies(
                show_type=data['type'][id], show_title=data['title'][id], director=data['director'][id],
                cast=data['cast'][id], country=data['country'][id], date_added=data['date_added'][id], release_year=data['release_year'][id],
                rating=data['rating'][id], duration=data['duration'][id]
                )
            bulk_data.append(movie_model)

            progress.next() 

        

        with transaction.atomic(): 
            Movies.objects.bulk_create(bulk_data)
            
        progress.finish() 


    def clear_database(self): 
        Movies.objects.all().delete() 
        




def populate_database(): 

    pop = PopulationUtils(cinema, cleanup=True)
    pop.save_to_model_csv('datasets/netflix_titles.csv') 



populate_database()


        
            

        







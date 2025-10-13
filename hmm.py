import os

file_name = 'GSE122497_series_matrix.txt'
class File:
    def __init__(self, file_name):
        self.file_name = file_name
    def extract(self):
        f = open(file_name, 'r')
        self.raw_text = f.read()
        f.close()
    
    '''
    future todo:
    1. extract function: get table and also if it's pos/neg
    2. get the other datasets, and scourge if you can find more
    3. code the REO extractor by how they did it
    
    '''
    

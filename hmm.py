import os

file_name = 'GSE122497_series_matrix.txt.gz'
class File:
    def __init__(self, file_name):
        self.file_name = file_name
    def extract(self):
        f = open(file_name, 'r')
        self.raw_text = f.read()
        f.close()
        
    

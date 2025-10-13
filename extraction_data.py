import os
import pandas as pd

class extract_data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.raw_text = ''
        self.binary_ov_arr = []
        self.raw_table = []
        
    def extract(self, debug):
        f = open(self.file_name)
        self.raw_text = f.read().splitlines()
        f.close()
        
        self.get_binary_ov_arr(debug)
        self.get_raw_table(debug)
        
        self.data = pd.DataFrame(self.raw_table, index = self.binary_ov_arr)
        
    def get_binary_ov_arr(self, debug):
        title_ind = 0
        while(self.raw_text[title_ind][0:13] != "!Sample_title"):
            title_ind+=1
        self.binary_ov_arr = []
        
        on = False
        current_string = ''
        for char in self.raw_text[title_ind]:
            if(char == '"'):
                if(not on):
                    on = True
                    current_string = ''
                else:
                    on = False
                    #print(current_string, end=" ")
                    if('cancer' not in current_string.lower() or 'non-cancer' in current_string.lower()):
                        self.binary_ov_arr.append(0)
                    elif('ovarian' in current_string.lower() or "OV" in current_string):
                        self.binary_ov_arr.append(1)
                    else:
                        self.binary_ov_arr.append(-1)
                continue
            if(on):
                current_string+=char
        if(debug):
            print('binary ov arr length (no of samples): ' + str(len(self.binary_ov_arr)))
            print('has a 1: ' + str(1 in self.binary_ov_arr))
            print('has a 0: ' + str(0 in self.binary_ov_arr))
            print('has a -1: ' + str(-1 in self.binary_ov_arr))
        
    def get_raw_table(self,debug):
        row_ind = 0
        while(self.raw_text[row_ind] != '!series_matrix_table_begin'):
            row_ind+=1
        row_ind+=2
        self.raw_table = {}
        for row in (self.raw_text[row_ind:-1]):
                #get the first element
            quote_ind = 1
            while(row[quote_ind] != '"'):
                quote_ind+=1
                
            elements = row.split("\t")[1:]
            elements = [elements for elements in elements if elements]
            self.raw_table[row[1:quote_ind]] = elements
        if(debug):
            print("preview of keys to raw table:" + list(self.raw_table.keys())[0] + ", " + list(self.raw_table.keys())[1])
            print("no of mirnas: " + str(len(self.raw_table)))
        # i only want ov cancer i do not want any other cancers
    '''
    future todo:
    1. extract function: get table and also if it's pos/neg
    2. get the other datasets, and scourge if you can find more
    3. code the REO extractor by how they did it
    
    '''

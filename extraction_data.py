import os
import pandas as pd

class extract_data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.raw_text = ''
        self.binary_ov_arr = []
        self.raw_table = []
        self.all_data = pd.DataFrame({})
        self.data = pd.DataFrame({})
        
    def extract(self, debug):
        f = open(self.file_name)
        self.raw_text = f.read().splitlines()
        f.close()
        
        self.get_binary_ov_arr(debug)
        self.get_raw_table(debug)
        
        self.all_data = pd.DataFrame(self.raw_table, index=self.df_index)
        
        self.filter(debug) #this determines self.data 
        self.clean_up_index(debug) #this determines self.cleaned_up_data
        
    def get_binary_ov_arr(self, debug):
        title_ind = 0
        while(self.raw_text[title_ind][0:13] != "!Sample_title"):
            title_ind+=1
        self.binary_ov_arr = []
        self.df_index = []
        
        on = False
        current_string = ''
        for char in self.raw_text[title_ind]:
            if(char == '"'):
                if(not on):
                    on = True
                    current_string = ''
                else:
                    on = False
                    
                    #get the sample index (remove the id at end)
                    space_ind = len(current_string) - 1
                    while(current_string[space_ind] != ' '):
                        space_ind-=1
                    self.df_index.append(current_string[:space_ind])

                    #classifying if it belongs. 1 is ov, 0 is healthy/benign, -1 is irrelevant
                    if("ovarian cancer" in current_string.lower()): # this excludes ovarian borderline and ov others bc <50 samples
                        self.binary_ov_arr.append(1)
                    elif('non-cancer' in current_string.lower() or 'benign ovarian disease' in current_string.lower()):
                        self.binary_ov_arr.append(0)
                    else:
                        self.binary_ov_arr.append(-1)
                continue
            if(on):
                current_string+=char
        if(debug):
            print('binary ov arr length (no of samples): ' + str(len(self.binary_ov_arr)))
            print('binary ov arr / sample index:')
            index_check = {}
            for i in range(len(self.binary_ov_arr)):
                index_check[self.df_index[i].split(" ", maxsplit=1)[0]] = self.binary_ov_arr[i]
            print(index_check)

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
    def filter(self,debug):
        self.bool_series = pd.Series([False if i == -1 else True for i in self.binary_ov_arr], index= self.df_index)
        self.data = self.all_data.loc[self.bool_series, :]

    def clean_up_index(self, debug):
        new_index = {}
        for i in set(self.data.index):
            if("ovarian cancer" in i.lower()): # this excludes ovarian borderline and ov others bc <50 samples
                new_index[i] = 1
            elif('non-cancer' in i.lower() or 'benign ovarian disease' in i.lower()):
                new_index[i]=0
        new_data = self.data.rename(index = new_index)
        return new_data

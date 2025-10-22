import os
import pandas as pd
import numpy as np

CONST_k = 0.95

# select significantly reversed miRNA pairs
f = open('kazuki_data.json')
non_cancer_data = pd.read_json(f, orient='split')

m_samples = non_cancer_data.shape[0]
n_mirnas = non_cancer_data.shape[1] #gets number of columns
miRNA_names_list = non_cancer_data.columns.tolist()

#list of each sample's expression stuff. key: mirna expression. value: mirna.  
og_dict = []
for i in range(0, m_samples):
    og_dict.append({})
    for j in range(0, n_mirnas):
        og_dict[i][m_samples.iloc[i, j]] = miRNA_names_list[j]

#take values in order (iterate through keys) and then assign values of order to them.
rankings_miRNAs = [] 
for i in range(0,n_mirnas):
    rankings_miRNAs.append({})
    miRNA_ranker_counter = 0
    for j in og_dict:
        og_dict[i][j] = miRNA_ranker_counter
        miRNA+=1
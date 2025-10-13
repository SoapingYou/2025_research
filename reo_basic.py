from extraction_data import extract_data
import os
import pandas as pd

os.chdir(r'/Users/sophieyu/Documents/GitHub/2025_research/')

# esophogeal and normal cases 
print('kazuki data:')
kazuki_data_extractor = extract_data("GSE122497_series_matrix.txt")
kazuki_data_extractor.extract(debug=False)
kazuki_data = kazuki_data_extractor.data 
print(kazuki_data.head)
print()

#ov cases and normal and other cancers 2
print('watara data:')
watara_data_extractor = extract_data("GSE113486_series_matrix.txt")
watara_data_extractor.extract(debug=True)
watara_data = watara_data_extractor.data
print(watara_data.head)
print()

# ov cases and normal and other cancers 1
print("yokoi data:")
yokoi_data_extractor = extract_data("GSE106817_series_matrix.txt")
yokoi_data_extractor.extract(debug=False)
yokoi_data = yokoi_data_extractor.data
print(yokoi_data.head)
print()

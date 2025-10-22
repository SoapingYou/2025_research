from extraction_data import extract_data
import os
import pandas as pd
import json

os.chdir(r'/Users/sophieyu/Documents/GitHub/2025_research/')

# esophogeal and normal cases 
print('kazuki data:')
kazuki_data_extractor = extract_data("GSE122497_series_matrix.txt")
kazuki_data_extractor.extract(debug=True)
kazuki_data = kazuki_data_extractor.clean_up_index(debug=True)
print(kazuki_data.head)
with open("kazuki_data.json", "w") as f:
    f.write(kazuki_data.to_json(orient="split"))


#ov cases and normal and other cancers 2
print('watara data:')
watara_data_extractor = extract_data("GSE113486_series_matrix.txt")
watara_data_extractor.extract(debug=True)
watara_data = watara_data_extractor.clean_up_index(debug=True)
print(watara_data.head)
with open("watara_data.json", "w") as f:
    f.write(watara_data.to_json(orient="split"))
# ov cases and normal and other cancers 1
print("yokoi data:")
yokoi_data_extractor = extract_data("GSE106817_series_matrix.txt")
yokoi_data_extractor.extract(debug=True)
yokoi_data = yokoi_data_extractor.clean_up_index(debug=True)
print(yokoi_data.head)
with open("yokoi_data.json", "w") as f:
    f.write(yokoi_data.to_json(orient="split"))



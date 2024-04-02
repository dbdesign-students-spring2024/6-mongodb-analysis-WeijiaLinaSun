import pandas as pd

file_path = 'listings.csv'
data = pd.read_csv(file_path)
l = ['host_id', 'name', 'price', 'host_is_superhost',
                           'neighbourhood', 'host_name',
                           'beds', 'review_scores_rating']
data = data.dropna(subset= l)  
data = data[l]

output_file_path = 'listings_clean.csv'
data.to_csv(output_file_path, index=False)


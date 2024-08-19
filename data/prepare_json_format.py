import pandas as pd
import json
import os
import yaml

with open("data_config.yaml") as file:
    yaml_data = yaml.safe_load(file)

dataset = "MIMIC"
original_data_path = yaml_data[dataset]["images_path_train"]
train_data_path = yaml_data[dataset]["train_csv"]
test_data_path = yaml_data[dataset]["test_csv"]

cols_to_keep = ['path', 'text']

train_df = pd.read_excel(train_data_path)
train_df = train_df[cols_to_keep]
train_df['path'] = train_df['path'].apply(lambda x: os.path.join(original_data_path, x))
# Rename path to image
train_df.rename(columns={'path': 'image'}, inplace=True)

test_df = pd.read_excel(test_data_path)
test_df = test_df[cols_to_keep]
test_df['path'] = test_df['path'].apply(lambda x: os.path.join(original_data_path, x))
# Rename path to image
test_df.rename(columns={'path': 'image'}, inplace=True)

data_list = train_df.to_dict('records')
with open('train_data.jsonl', 'w') as f:
    for item in data_list:
        f.write(json.dumps(item) + '\n')

data_list = test_df.to_dict('records')
with open('test_data.jsonl', 'w') as f:
    for item in data_list:
        f.write(json.dumps(item) + '\n')
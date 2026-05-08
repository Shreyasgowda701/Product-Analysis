import kagglehub
import os
import pandas as pd

path = kagglehub.dataset_download(
    "rivalytics/saas-subscription-and-churn-analytics-dataset"
)

files = os.listdir(path)

dataframes = {}

for file in files:
    if file.endswith(".csv"):
        main_files = "_".join(file.split("_")[1:])
        print(main_files)
        full_path = os.path.join(path,file)
        df = pd.read_csv(full_path)
        df.to_csv(main_files, index=False)
        dataframes[main_files] = df

print(dataframes.keys())
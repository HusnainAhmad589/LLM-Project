import kagglehub
import pandas as pd
import os

DATASET_ID = "thevirusx3/automated-essay-scoring-dataset"

def load_kaggle_dataset():
    path = kagglehub.dataset_download(DATASET_ID)

    # Dataset folder ke andar CSV dhundo
    for file in os.listdir(path):
        if file.endswith(".csv"):
            csv_path = os.path.join(path, file)
            return pd.read_csv(csv_path)

    raise FileNotFoundError("No CSV file found in Kaggle dataset")
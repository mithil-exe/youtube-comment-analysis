import pandas as pd

def load_comments(path):
    df = pd.read_csv(path)
    df = df.rename(columns={df.columns[0]: "Comment"})
    return df

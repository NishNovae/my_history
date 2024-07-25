import pandas as pd

def read_data(path='~/db/parquet'):
    df = pd.read_parquet(path)

def top():
    df = read_data()
    fdf = df[df['dt'] == '2024-07-12']
    sdf = fdf.sort_values(by='cnt', ascending=False)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[df['dt'].equals(query)]

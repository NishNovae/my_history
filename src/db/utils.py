import pandas as pd

def read_data(path='~/db/parquet'):
    df = pd.read_parquet(path)
    return df

def top(num=5, date='2024-07-12'):
    df = read_data()
    fdf = df[df['dt'] == date]
    sdf = fdf.sort_values(by='cnt', ascending=False)
    sdf = sdf.head(num)    

    ddf = sdf.drop(columns=['dt'])
    tdf = ddf.head(num)

    r = tdf.to_string(index=False)
    return r

def count(query):
    df = read_data()
    fdf = df[ df['cmd'] == query ]
    cnt = fdf['cnt'].sum()
    return cnt

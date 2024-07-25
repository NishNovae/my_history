import sys
import pandas as pd

def cnt(q):
    df = read_parquet()
    fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()
    return cnt

#def read_parquet():
#    df = pd.read_parquet("~/tmp/history.parquet")
#    return df

def read_parquet(path="~/tmp/history.parquet"):
    df = pd.read.parquet(path)
    return df

def query():
    q = sys.argv[1]
    i = cnt(q)
    print(f"질의: {q}에 대한 결과는 {i}입니다.")
    print("질의:%s에 대한 결과는 %s 입니다." % (q, i))
    print("질의:%10s에 대한 결과는 %d 입니다" % (q, i))

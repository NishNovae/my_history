import sys
import pandas as pd

def cnt():
    args = sys.argv
    try:
        if len(args) != 2:
            print("ERROR: requires one in-line argument. Please try again.")
        else:
            try:
                df = pd.read_parquet("~/tmp/history.parquet")
                fdf = df[df['cmd'].str.contains(args[1])]
                cnt = fdf['cnt'].sum()
                print(cnt)
            except:
                print("Something went wrong...")
    except AttributeError:
        print("ERROR: sys.argv does not exist. The script should be run from the command line with in-line arguments.")
        

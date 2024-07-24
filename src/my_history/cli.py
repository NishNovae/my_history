import sys
import pandas as pd
<<<<<<< HEAD

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
            except ValueError:
                print("Something went wrong...")
    except AttributeError:
        print("ERROR: sys.argv does not exist. The script should be run from the command line with in-line arguments.")
        
=======
import argparse

PARQ_PATH="/home/nishtala/db/parquet/"

def argv():
    parser = argparse.ArgumentParser(description="history search program")
    
    group = parser.add_argument_group()

    group.add_argument("-c", "--count", type=str, help="mh -c keyword")

    group.add_argument("-t", "--top", nargs=2, help="mh -t num <YYYY-MM-DD>")
 
    args = parser.parse_args()

    if args.count:
        cnt_count(args.count)
    elif args.top:
        cnt_top(args.top)
    else:
        parser.print_help()

def cnt_count(keyword):
    df = pd.read_parquet(PARQ_PATH)
    fdf = df[ df['cmd'].str.contains(keyword) ]
    cnt = fdf['cnt'].sum()
    print(f"Keyword: {keyword} was used {cnt} times.")

def cnt_top(args):          # list of 2 elements [0], [1]
    num = int(args[0])
    date = args[1]

    df = pd.read_parquet(PARQ_PATH)
    fdf = df[df['dt'] == date].sort_values(by='cnt', ascending=False)
    fdf.index = range(1, len(fdf) +1)

    print(f"Printing top {num} commands from date {date}...")
    print("================================================")
    print(fdf.head(num))
#argv()
>>>>>>> fe3b1b0 (vers)

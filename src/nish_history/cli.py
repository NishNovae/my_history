import argparse
from db.utils import count, top

def cmd():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount', type=str)
    parser.add_argument('-t', '--top', type=int)  
    parser.add_argument('-d', '--dt', type=str)
    args = parser.parse_args()    

    if args.scount:
        cnt = count(args.scount)
        print(f"The command {args.scount} was used {cnt} times.")

    elif args.top:
        if args.dt:
            print(top(args.top, args.dt)) 
        else:
            print("TODO")
            parser.error("ERROR: -t option must work with -d option.")

    else:
        parser.print_help()

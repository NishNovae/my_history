import argparse

def hello_msg():
    return "hello"

# the function that runs when pytest is called
def cmd():
#    msg = hello_msg()
#    print(msg)
    
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    
    parser.add_argument('-s', '--scount')
    parser.add_argument('-t', '--top')  
    parser.add_argument('-d', '--dt')

    args = parser.parse_args()

    if args.scount:
        print(f"-s => {args.scount}")

    elif args.top:
        print(f"-t => {args.scount}")
        if args.dt:
            print(f"-d => {args.scount}")
        else:
            print("TODO")
            parser.error("ERROR: -t option must work with -d option.")

    else:
        parser.print_help()




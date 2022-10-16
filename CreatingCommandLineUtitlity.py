"""
What is comand Line utility:
    1) ye command pe run hoga jo value dege uske hisab se
"""

import argparse  # help for command line utility
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


# How to exicute:
"""
Step 1) open windows power shell in start button.
step 2) then write cd ~
step 3) then cd .\PycharmProjects\
setp 4) then cd .\firstprog\
step 5) ten python .\CreatingCommandLineUtitlity.py --x 2 --y 2 --o add 
"""
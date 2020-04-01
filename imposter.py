import argparse


welcomeMsg = "Welcome! this is a test arg parser"
parser = argparse.ArgumentParser(description=welcomeMsg)


parser.add_argument('--domain', '-d', required=True, help='domain name of the website you want to scrape. i.e. “https://ahadsheriff.com"')
parser.add_argument('--ofile', '-o', help='define output file to save results of stdout. i.e. "output.txt"')
parser.add_argument('--lines', '-l', help='number of lines of output to print to the console"', type=int)
parser.add_argument('--eito', '-e', help='This is an experiment, I can do anything"', type=int)

args = parser.parse_args()
domain = args.domain
ofile = args.ofile
lines = args.lines

#How to deal with optional parameters
if args.eito:
    print("eito mode is enabled")

print("domain:", domain)
print("output file:", ofile)
print("lines:", lines)


parser.parse_args()
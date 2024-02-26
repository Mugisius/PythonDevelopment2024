import cowsay
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("message", nargs="*", type=str)
parser.add_argument('-e', default=cowsay.Option.eyes, type=str)
parser.add_argument("-f", dest="file", action="store", default="default", type=str)
args = parser.parse_args()

if args.message:
    message = [w for arg in args.message for w in arg.split(" ") if w]
    message = " ".join(message)
else:
    message = "".join(sys.stdin.readlines())

print(cowsay.cowsay(message,eyes=args.e[:2],cow=args.file))

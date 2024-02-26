import cowsay
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("message", nargs="*", type=str)
parser.add_argument('-e', default=cowsay.Option.eyes, type=str)
parser.add_argument("-f", dest="file", action="store", default="default", type=str)
parser.add_argument("-l", action="store_true")
parser.add_argument("-n", action="store_false")
parser.add_argument("-T", type=str, default=cowsay.Option.tongue)
parser.add_argument("-W", type=int, default=40)

parser.add_argument("-b", const="b", dest="preset", action="append_const")
parser.add_argument("-d", const="d", dest="preset", action="append_const")
parser.add_argument("-g", const="g", dest="preset", action="append_const")
parser.add_argument("-p", const="p", dest="preset", action="append_const")
parser.add_argument("-s", const="s", dest="preset", action="append_const")
parser.add_argument("-t", const="t", dest="preset", action="append_const")
parser.add_argument("-w", const="w", dest="preset", action="append_const")
parser.add_argument("-y", const="y", dest="preset", action="append_const")

args = parser.parse_args()

if args.l:
    print("Cow files:")
    print(" ".join(sorted(cowsay.list_cows())))
    exit(0)

if args.preset:
    args.preset = args.preset[-1]

if args.message:
    if not args.n:
        parser.print_help()
        exit(0)
    message = [w for arg in args.message for w in arg.split(" ") if w]
    message = " ".join(message)
else:
    message = "".join(sys.stdin.readlines())

print(cowsay.cowsay(
        message, 
        eyes=args.e[:2], 
        cow=args.file,
        wrap_text=args.n, 
        tongue=args.T[:2], 
        width=(args.W-1),
        preset=args.preset
        ))

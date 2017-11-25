import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sa", help="Your shared 16-bit secret with Alice", type=int)
parser.add_argument("--sb", help="Your shared 16-bit secret with Bob", type=int)
parser.add_argument("--da", help="The data broadcasted by Alice", type=int)
parser.add_argument("--db", help="The data broadcasted by Bob", type=int)
parser.add_argument("--m", help="The message you may want to send", type=int)
parser.add_argument("--b", help="1 for sending message m, 0 for not sending it", type=int)

args = parser.parse_args()
print(args.sa, args.sb, args.da, args.db)

# print('0C73')
# test = str(bin(int('0C73', 16)))
# print(test[:4])
# print(int('0C73', 16))
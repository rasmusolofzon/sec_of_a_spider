import sys
import math

def get_code(points):
	sum = 0
	for i in points.keys():
		print(i)
		prod = 1
		for j in points.keys():
			if j != i:
				print(j)
				prod *= j / (j - i)
		sum += points[i] * prod
	return round(sum)


if __name__ == '__main__':

	k = int(sys.argv[1])
	n = int(sys.argv[2])
	f1 = [int(x) for x in sys.argv[3].split(',')]
	shares = [int(x) for x in sys.argv[4].split(',')]
	partners = [int(x) for x in sys.argv[5].split(',')]
	partner_points = [int(x) for x in sys.argv[6].split(',')]

	if k >= 3 and k < n and n <= 8 and len(f1) == k:

		points = {}
		points[1] = sum(f1) + sum(shares)
		for i in range(len(partners)):
			points[partners[i]] = partner_points[i]

		f0 = get_code(points)
		print(f0)

	else:
		print('3 <= k < n <= 8 and the specified polynomial must be of order k-1')
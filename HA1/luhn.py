import sys

def get_censored_digit(cc_nbr):
	digit_sum = 0
	censored_digit_pos = 0
	censored_digit_factor = 0
	nbr_digits = len(cc_nbr)
	parity = nbr_digits % 2
	for i in range(nbr_digits):
		if i % 2 == parity:
			if cc_nbr[i] == 'X':
				censored_digit_factor = 2
			else:
				product = int(cc_nbr[i]) * 2
				if product > 9:
					product = product - 9
				digit_sum = digit_sum + product
		else:
			if cc_nbr[i] == 'X':
				censored_digit_factor = 1
			else:
				product = int(cc_nbr[i]) * 1
				digit_sum = digit_sum + product
	for i in range(10):
		product = i * censored_digit_factor
		if product > 9:
			product = product - 9
		if (digit_sum + product) % 10 == 0:
			return i


def get_censored_digits(censored_cc_nbrs):
	censored_digits = ''
	for cc_nbr in censored_cc_nbrs:
		censored_digits = censored_digits + str(get_censored_digit(cc_nbr))
	return censored_digits


def check_cc_nbr(cc_nbr):
	digit_sum = 0
	nbr_digits = len(cc_nbr)
	parity = nbr_digits % 2
	for i in range(nbr_digits):
		digit = int(cc_nbr[i])
		if i % 2 == parity:
			digit = digit * 2
			if digit > 9:
				digit = digit - 9
		digit_sum  = digit_sum + digit
	return digit_sum % 10 == 0


def verify_digits(censored_digits, censored_cc_nbrs):
	for i in range(len(censored_cc_nbrs)):
		complete_cc_nbr = censored_cc_nbrs[i].replace('X', str(censored_digits[i]))
		if not check_cc_nbr(complete_cc_nbr):
			return False
	return True
	

if __name__ == '__main__':
	censored_cc_nbrs = []
	filename = sys.argv[1]
	with open(filename) as file:
	    for line in file:
	    	censored_cc_nbrs.append(line.strip())
	censored_digits = get_censored_digits(censored_cc_nbrs)
	print(censored_digits)
	print(verify_digits(censored_digits, censored_cc_nbrs))

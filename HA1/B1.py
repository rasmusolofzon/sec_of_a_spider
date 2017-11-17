import sys

def luhn(card_nbr):
    split_nbr = {}
    n = len(card_nbr)
    for i in range(n):
        split_nbr[i] = int(card_nbr[i:i+1])
    
    for i in range(2, n, 2):
        split_nbr[n-i] *= 2
        if split_nbr[n-i] > 9:
            split_nbr[n-i] -= 9
        i += 1
    
    sum_digits = sum(list(split_nbr.values())[:])
    
    return sum_digits % 10

def make_luhn(card_X_nbr):

    for i in range(10):

        if luhn(card_X_nbr) == 0:
            return 1
    
    return 0
    

if __name__ == '__main__':
    print(sys.argv)

    censored_list = []
    answer_string = ""
    
    try:
        list_file = open(sys.argv[1], 'r') 
    except:
        print("Which file?", end='\n\n')
        sys.exit(42)

    for line in list_file:
       censored_list.append(line) 
    
    for card_nbr in censored_list:
        print('', end='')
        digit = 0

        answer_string += str(digit)

    print(luhn("79927398713"))
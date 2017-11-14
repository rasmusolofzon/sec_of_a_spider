import sys

def luhn(card_nbr):
    split_nbr = {}
    for i in range(10):
        split_nbr[i] = int(card_nbr[i:i+1])
    
    for i in range(1, 6):
        split_nbr[10-i*2] += 2
        if split_nbr[10-i*2] > 9:
            split_nbr[10-i*2] -= 9
    
    sum_digits = sum(split_nbr.values()[:-1])
    
    return card_nbr

def make_luhn(card_X_nbr):

    for i in range(10):

        if luhn(card_X_nbr) == 0:
            return 1
    

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
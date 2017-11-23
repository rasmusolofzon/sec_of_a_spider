
def luhn(card_nbr):
    split_nbr = {}
    n = len(card_nbr)

    for i in range(n-1):
        split_nbr[i] = int(card_nbr[i:i+1])
    
    for i in range(n-2, -1, -2):
        # print("\n{0}".format(split_nbr[i]))
        split_nbr[i] *= 2
        if split_nbr[i] > 9:
            split_nbr[i] -= 9
        # print("{0}\n".format(split_nbr[i]))
        # i += 1
    
    sum_digits = sum(list(split_nbr.values()))
    print(sum_digits)
    
    return True if sum_digits % 10 == 0 else False

def validate_nbr(card_nbr):
    split_nbr = {}
    n = len(card_nbr)

    for i in range(n-1):
        split_nbr[i] = int(card_nbr[i:i+1])
        # print(split_nbr[i], end="")
    # print()
    
    for i in range(n-2, -1, -2):
        # print("\n{0}".format(split_nbr[i]))
        split_nbr[i] *= 2
        # if split_nbr[i] > 9:
        #     split_nbr[i] -= 9
        # print("{0}\n".format(split_nbr[i]))
    
    summ = 0
    for digit in split_nbr.values():
        # print(digit)
        if digit > 10:
            summ += 1 + (digit-10) 
        else:
            summ += digit
        # print(summ, end='\n\n')
    
    # print(summ)
    
    return True if summ % 10 == 0 else False

if __name__ == '__main__':
    censored_list = []
    answer_string = ""

    with open("luhn_nbrs.txt", 'r') as f:
        for line in f:
            censored_list.append(line) 
    
        new_list = []

        for card_nbr in censored_list:
            print("{0}".format(card_nbr[:-1]))
            digit = 0

            for i in range(len(card_nbr)):
                if card_nbr[i] == 'X':
                    for j in range(10):
                        test = card_nbr[:i] + str(j) + card_nbr[i+1:]
                        if validate_nbr(test):
                        # if luhn(test):
                            # print(validate_nbr(test))
                            print(luhn(test))
                            digit = j
                            # print("{0} = {1}".format(digit, j))
                            new_list.append(test)
                            print("{0}".format(test))

            answer_string += str(digit)
        
        for nbr in new_list:
            print(nbr, end='')

        print()
        print(answer_string)
        print(len(answer_string))


    # print("Success!" if validate_nbr("79927398713") else "Fail!")
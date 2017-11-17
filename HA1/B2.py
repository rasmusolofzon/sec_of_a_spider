# TODO: write confidence_interval function
# TODO: write generate_coins function

import scipy.stats as stats
import numpy

def confidence_interval(x_hat, sigma, n, gamma=3.66):
    ci = 0
    
    return "nada"

if __name__ == '__main__':
    u = 16 # number of bits used for ID of bin
    k = 2 # number of collisions needed to make a coin
    c = 1 # target, the number of coins to create. Can be one of [1, 100, 10000]

    coin_list = [] # a list w/ created coins
    tossed_balls = {} # a dictionary where keys are computed hashes and the values the x:es that result in the key hash value

#print(numpy.mean(test))

'''
    # a sort-of pseudocode sketch

    while len(coinsList) < c
        randomize r
        calc h(r)
        dict[h(r)].append(r) # plus an empty-key-check
        if len(dict[h(r)]) == k:
            coinsList.append(h(r))
    
    # example values output from test quiz
    c = 10000
    u = 20
    k = 7
    confidence interval width = 4783

    c = 1
    u = 16
    k = 2
    confidence interval width = 22

'''
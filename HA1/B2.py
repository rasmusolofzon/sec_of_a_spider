import math
import statistics

def confidence_interval(x_hat, sigma, n, gamma=3.66):
    ci = 0
    
    return "nada"

def generate_coins(u, k, c):

    return "coins!"

if __name__ == '__main__':
    u = 16 # number of bits used for ID of bin
    k = 2 # number of collisions needed to make a coin
    c = 1 # target, the number of coins to create. Can be one of [1, 100, 10000]
    ci_width = 22
    ci = math.inf

    coin_list = [] # a list w/ created coins
    tossed_balls = {} # a dictionary where keys are computed hashes and the values the x:es that result in the key hash value

    while ci > ci_width:
        #generate_coins(u, k, c)
        #ci = confidence_interval(blablabla)
        pass
    
    test = [1, 2, 3, 4, 5]
    print(statistics.mean(test))
    print(statistics.stdev(test))
    print(statistics.variance(test))

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
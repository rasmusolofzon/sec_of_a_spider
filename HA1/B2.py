import math
import statistics
import hashlib
import random

def confidence_interval(iterations_list):
    #x_hat, sigma, n, gamma=3.66
    n_squared = math.sqrt(len(iterations_list))
    s = statistics.stdev(iterations_list)
    gamma = 3.66
    x_hat = statistics.mean(iterations_list)  
    ci =  gamma*s/n_squared
    print(ci)
    return ci

def generate_coins(u, k, c):
    coin_list = [] # a list w/ created coins
    # a dictionary where keys are computed hashes and the values 
    # the x:es that result in the key hash value
    tossed_balls = {} 
    iterations = 0

    while len(coin_list) < c:
        x = random.randrange(255).to_bytes(2, byteorder="big")
        h = hashlib.md5(x).digest()
        mask = 0b1
        for i in range(u):
            mask = mask | (0b1 << i)
        #print(len(bin(int.from_bytes(h, byteorder="big"))))
        #print(bin(int.from_bytes(h, byteorder="big")))
        h = int.from_bytes(h, byteorder="big") & mask
        #print(bin(mask))
        #print(bin(h))
        #print(h)

        if h not in tossed_balls.keys():
            tossed_balls[h] = [x]
        else:
            tossed_balls[h].append(x)
            if len(tossed_balls[h]) == k:
                coin_list.append(h)
        iterations += 1

    return iterations

if __name__ == '__main__':
    u = 16 # number of bits used for ID of bin
    k = 2 # number of collisions needed to make a coin
    c = 1 # target, the number of coins to create. Can be one of [1, 100, 10000]
    ci_width = 22
    ci = math.inf
    iterations_list = []

    while ci > ci_width:
        iterations_list.append(generate_coins(u, k, c))
        if len(iterations_list) > 1:
            ci = confidence_interval(iterations_list)
        pass
    
    print(iterations_list)
    print("Mean of iterations: ", end="")
    print(statistics.mean(iterations_list))
    print("Standard deviation of iterations: ", end="")
    print(statistics.stdev(iterations_list))
    print("Median of iterations: ", end="")
    print(statistics.median(iterations_list))

    
    # test = [1, 2, 3, 4, 5]
    # print(statistics.mean(test))
    # print(statistics.stdev(test))
    # print(statistics.variance(test))

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
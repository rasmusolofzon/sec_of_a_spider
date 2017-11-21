import math
import statistics
import hashlib
import random
import time

def confidence_interval(iterations_list):
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
        # x = random.getrandbits(u).to_bytes(3, byteorder="big")
        x = random.getrandbits(4*8)
        x = x.to_bytes(4, byteorder="big")
        h = hashlib.md5(x).digest()
        mask = 0b1
        for i in range(u):
            mask = mask | (0b1 << i)
        h = int.from_bytes(h, byteorder="big") & mask

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
    ci_width = 22 # the target width of confidence interval

    # a dictionary to facilitate switching between test values;
    # the parameters in the tuples are the following:
    # (u, k, c, ci_width)
    parameters = {  1: (16, 2, 1, 22),
                    2: (16, 2, 100, 24),
                    3: (16, 2, 10000, 22),
                    4: (20, 7, 1, 79671),
                    5: (20, 7, 100, 15616),
                    6: (20, 7, 10000, 4783) }
    # choose combination of test parameters here:
    combination = 1

    ci = math.inf
    iterations_list = []

    start_time = time.time()
    
    while ci > parameters[combination][3]:
        iterations_list.append(generate_coins(parameters[combination][0], 
                                parameters[combination][1], 
                                parameters[combination][2]))
        if len(iterations_list) > 5:
            ci = confidence_interval(iterations_list)
    
    end_time = time.time() - start_time
    
    print("\nThis took {0} iterations:\n{1}\n".format(len(iterations_list), iterations_list))
    print("Mean of iterations: \t\t\t{0}".format(statistics.mean(iterations_list)))
    print("Standard deviation of iterations: \t{0}".format(statistics.stdev(iterations_list)))
    print("Median of iterations: \t\t\t{0}".format(statistics.median(iterations_list)))
    print("Time for execution: \t\t\t{0}\n".format(end_time))

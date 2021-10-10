# prime_mutiprocessing.py

import multiprocessing
import time
import math
from multiprocessing import freeze_support


'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
    with multiprocessing.Pool(processes=n_processors) as pool:
        return pool.map(func, i)

'''Define task function'''
def is_prime(n):
    if (n < 2) or (n % 2 == 0 and n > 2):
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def fatorial(n):
    return f"{n} >> {math.factorial(n)}"

def main():
    start = time.perf_counter()

    '''
    set up parameters required by the task
    '''
    num_max = 10000000
    n_processors =20
    x_ls = list(range(num_max))

    '''
    pass the task function, followed by the parameters to processors
    '''
    out = run_multiprocessing(fatorial, x_ls, n_processors)
    end = time.perf_counter()
    print("Input length: {}".format(len(x_ls)))
    print("Output length: {}".format(len(out)))	
    #print("Mutiprocessing time: {}mins\n".format((end-start)/60))
    print("Mutiprocessing time: {}secs\n".format((end-start)))
    #print(out)

if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()
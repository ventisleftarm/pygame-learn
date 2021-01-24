#import numpy as np
import math
import random
import matplotlib.pyplot as plt
import timewrapper as twr


@twr.timeit
def square_running(number):
    for i in range(number):
        for j in range(number):
            math.sqrt(number)


#square_running(100)

#square_running(1000)

#square_running(10000)


def return_random_list(length_of_list):

    Start = 9
    Stop = 99
    return [random.randint(Start, Stop) for iter in range(length_of_list)]

print(return_random_list(20))


@twr.timeit
def sort_list(unsorted_list):
    return unsorted_list.sort()


sort_list(return_random_list(10000))
sort_list(return_random_list(100000))
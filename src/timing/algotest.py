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
def sort_list(unsorted_list, **kwargs):
    return unsorted_list.sort()

time_list = []
length_list = [1e5,2e5,5e5,1e6,2e6,5e6]
for i in length_list:
    logtime_data ={}
    sort_list(return_random_list(int(i)), log_time=logtime_data)
    print(logtime_data)
    time_list.append(logtime_data["SORT_LIST"])
plt.plot(length_list, time_list, "x")
plt.xlabel("length of list")
plt.ylabel("time to sort (seconds)")
plt.show()

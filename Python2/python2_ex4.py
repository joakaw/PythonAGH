import random
from multiprocessing import Pool
import multiprocessing as mp
from multiprocessing import Process, freeze_support
from multiprocessing import Lock, Array


def createList():
    new_list = []
    for i in range(0, 100):
        new_list.append(random.randint(0, 39))
    return new_list


def createHistogram():
    hist_list = [0] * 40
    return hist_list


def hist(some_list, histogram, lk):
    for l in some_list:
        histogram[l] = histogram[l] + 1
    return histogram


if __name__ == '__main__':
    freeze_support()

    l = Lock()
    pool = Pool(processes=2)

    created_list = createList()
    print("Created list: ", created_list)
    created_empty_histogram = createHistogram()
    print("Created empty histogram: ", created_empty_histogram)
    created_histogram = hist(created_list, created_empty_histogram, l)
    print("Created histogram: ", created_histogram )

    arr = Array('i', range(40))
    for k in range(0, 40):
        arr[k] = 0

    p1 = Process(target=hist, args=(created_list[0:50], arr, l))
    p2 = Process(target=hist, args=(created_list[50:100], arr, l))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    for i in range(0, 40):
        print(arr[i] - created_histogram[i])

    for i in range(0, 40):
        print(arr[i])

""" example script of multiprocessing module in python"""

import multiprocessing
import time

LETTERS = "A" * 100

def f(s, num=1):
    for i in range(10**6):
        1 == 1 + num
    print(s, end="")


def f_(zipped):
    (s, num) = zipped
    for i in range(10**6):
        1 == 1 + num
    print(s, end="")


def single_thread():
    t0 = time.time()
    for letter in LETTERS:
        f(letter)
    return time.time() - t0


def multi_thread(n_threads):
    t0 = time.time()
    p = multiprocessing.Pool(n_threads)
    p.map(f_, zip(list(LETTERS), [1]*len(LETTERS)))
    return time.time() - t0


def main():
    print("\nsingle thread run time %s" %single_thread())
    for n in range(1, 21):
        print("multiple thread run time with %d thread is %s" %(n, multi_thread(n)))



if __name__ == "__main__":
    main()

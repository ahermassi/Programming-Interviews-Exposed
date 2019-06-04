"""
Python 3 implementation of insertion sort algorithm
"""


def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]  # this is the key element to insert
        j = i - 1  # start looking to the back (previous element)
        while j >= 0 and l[j] > key:  # while still looking back and the previous element is greater than the key...
            l[j + 1] = l[j]  # shift that greater element to the right
            j -= 1  # one more step back
        l[j + 1] = key  # a smaller element is found; insert the key after it

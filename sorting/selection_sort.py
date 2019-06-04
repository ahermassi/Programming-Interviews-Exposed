"""
Python 3 implementation of selection sort algorithm
"""


def selection_sort(l):
    for i in range(len(l)):
        min_index = find_min_index(l, i)  # find index of smallest element in l[i:], l[i+1:],...
        l[i], l[min_index] = l[min_index], l[i]  # swap smallest element with first element of the sub-list l[i:]


def find_min_index(l, i):
    """
    Find the index of the smallest element in list[i:]
    :param l: list to search
    :param i: first index
    :return: index of smallest element
    """
    min_index = i
    for j in range(i + 1, len(l)):
        if l[j] < l[min_index]:
            min_index = j
    return min_index

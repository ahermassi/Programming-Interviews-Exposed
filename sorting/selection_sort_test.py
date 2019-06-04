from array import array

from selection_sort import selection_sort

if __name__ == '__main__':
    A = array('i', [64, 25, 12, 22, 11])
    print("Original array: ", A.tolist())
    selection_sort(A)
    print("Sorted array: ", A.tolist())

import sys

if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5, 6]]
    l1 = [[]]

    # print(len(l1))
    # print(sys.getrecursionlimit())
    #
    # l2 = [[]] * 5
    # print(l2)

    # print("A".casefold())

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    fruits.sort(key=len)
    print(fruits)

    s = 'apple'
    print(s[::-1])

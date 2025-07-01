
def binarySearch(array, x):
    low = 1
    high = len(array) -1
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def find_pair(lst: list, ct):
    if len(lst) == 0:
        return print(ct)

    else:
        pair = abs(2147483647 - lst[0])
        if binarySearch(lst, pair) != -1:
            lst.pop(binarySearch(lst, pair))

        lst.pop(0)
        find_pair(lst, ct + 1)


for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split(" "))))

    try:
        find_pair(a, 0)

    except Exception as e:
        print(e)
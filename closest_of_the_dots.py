# closets of the dots in 2D page
# implementation in O(n*log(n)) with trick of sorting dots base on y coordinate at the begin of the program

from math import sqrt
import sys

FLT_MAX = sys.float_info.max


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1, p2):
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def brute_force(p, local_n):
    local_min = FLT_MAX;
    for i in range(local_n):
        for j in range(i + 1, local_n):
            if dist(p[i], p[j]) < local_min:
                local_min = dist(p[i], p[j])
    return local_min


def my_min(x, y):
    if x < y:
        return x
    else:
        return y


def strip_closest(strip, size, d):
    local_min = d

    for i in range(size):
        for k in range(i + 1, size):
            if (strip[k].y - strip[i].y) < local_min:
                if (strip[k].y - strip[i].y) < local_min:
                    if dist(strip[i], strip[k]) < local_min:
                        local_min = dist(strip[i], strip[k])
            else:
                break
    return local_min


def closest_util(px, py, size):
    if size <= 3:
        return brute_force(px, size)
    mid = int(size / 2)
    mid_point = px[mid]

    pyl = []
    pyr = []
    for i in range(mid):
        pyl.append(0)
    for i in range(size - mid):
        pyr.append(0)
    li = 0
    ri = 0
    for i in range(size):
        if py[i].x <= mid_point.x:
            pyl[li] = py[i]
            li += 1
        else:
            pyr[ri] = py[i]
            ri += 1

    dl = closest_util(px, pyl, mid)
    px2 = []
    for i in range(px.__len__()):
        if i >= mid:
            px2.append(px[i])
    dr = closest_util(px2, pyr, size - mid)

    d = my_min(dl, dr)

    strip = []
    j = 0
    for i in range(size):
        if abs(py[i].x - mid_point.x) < d:
            strip.append(py[i])
            j += 1

    return my_min(d, strip_closest(strip, j, d))


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def Qsort(array, low, high, condition):
    arr = []
    for i in range(low, high + 1):
        if condition:
            arr.append(array[i].x)
        else:
            arr.append(array[i].y)

    if low < high:
        pi = partition(arr, low, high)

        qsort(arr, low, pi - 1)
        qsort(arr, pi + 1, high)


def qsort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        qsort(arr, low, pi - 1)
        qsort(arr, pi + 1, high)


def closest(array, length):
    px = []
    py = []
    for i in range(length):
        px.append(array[i])
        py.append(array[i])

    Qsort(px, 0, length - 1, True)
    Qsort(py, 0, length - 1, False)

    return closest_util(px, py, length)


p = [Point(2, 3), Point(29, 30), Point(40, 58), Point(5, 7), Point(11, 10), Point(3, 9)]
n = p.__len__()
print("The smallest distance is " + closest(p, n).__str__())

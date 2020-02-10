#!/bin/python3
from itertools import combinations


def totalTriplets(capacity, desiredCapacity):
    l = len(capacity)
    count = 0
    ind = []
    for i in range(l):
        ind.append(i)
    #     get the combinations of indexes
    indexcombi = combinations(ind, 3)
    for j in indexcombi:
        if (j[0] + 1 == j[1] or j[1] + 1 == j[2]):
            if capacity[j[0]]*capacity[j[1]]*capacity[j[2]] == desiredCapacity:
                count+=1
    return count

if __name__ == '__main__':
    result = totalTriplets([1, 2, 2, 2, 4], 8)

    print(result)

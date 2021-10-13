# solution https://codeforces.com/problemset/problem/1535/B

import math

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    evenA, oddA = [], []
    for number in a:
        if number % 2:
            oddA.append(number)
        else:
            evenA.append(number)
    a.clear()
    a = sorted(evenA) + sorted(oddA)

    count = 0
    for j in range(len(a)):
        for k in range(j + 1, len(a)):
            if math.gcd(a[j], a[k] * 2) > 1:
                count += 1
    print(count)

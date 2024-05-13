# https://codeforces.com/problemset/problem/1972/A

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    count = 0
    for j in range(len(a)):
        if a[j] > b[j]:
            del a[-1]
            a.insert(j, b[j])
            count += 1
    print(count)
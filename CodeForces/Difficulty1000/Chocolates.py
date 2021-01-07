# solution https://codeforces.com/problemset/problem/1139/B

n = int(input())
a = [int(x) for x in input().split()]

a.reverse()

x = 0
for i in range(len(a) - 1):
    if a[i + 1] == a[i]:
        a[i + 1] -= (a[i + 1] - a[i] + 1)
    elif a[i + 1] > a[i]:
        a[i + 1] = a[i] - 1
        if a[i + 1] < 0:
            a[i + 1] = 0

    x += a[i]

print(x + a[len(a) - 1])

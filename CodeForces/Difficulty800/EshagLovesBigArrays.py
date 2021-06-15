# solution https://codeforces.com/problemset/problem/1529/A

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(len(a) - a.count(min(a)))

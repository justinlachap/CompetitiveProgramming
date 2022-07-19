# https://codeforces.com/contest/1703/problem/B

t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    accu = []
    points = 0
    for j in s:
        if j not in accu:
            points += 2
            accu.append(j)
        else:
            points += 1

    print(points)
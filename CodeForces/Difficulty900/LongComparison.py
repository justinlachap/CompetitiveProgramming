# solution https://codeforces.com/problemset/problem/1613/A

t = int(input())

for i in range(t):
    x1, p1 = input().split()
    x2, p2 = input().split()
    diff = int(p1) - int(p2)
    x1 = int(x1)
    x2 = int(x2)
    if (diff > 0):
        x1 *= (10 ** (diff))
    elif (diff < 0):
        x2 *= (10**(-diff))
    if (x1 > x2):
        print('>')
    elif (x2 > x1):
        print('<')
    else:
        print('=')

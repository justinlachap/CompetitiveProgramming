# https://codeforces.com/contest/1703/problem/C

t = int(input())

for i in range(t):
    n = int(input())

    a = [int(x) for x in input().split()]
    out = []
    for j in range(n):
        nOp, ope = input().split()
        final = a[j]
        for k in ope:
            if k == 'D':
                if final == 9:
                    final = 0
                else:
                    final += 1
            if k == 'U':
                if final == 0:
                    final = 9
                else:
                    final -= 1
        out.append(final)
    print(*out)
# solution https://codeforces.com/problemset/problem/1598/A

t = int(input())

for i in range(t):
    n = int(input())
    firstRow, secondRow = input(), input()
    for j in range(n):
        if firstRow[j] == '1' and firstRow[j] == secondRow[j]:
            print("NO")
            break
    else:
        print("YES")

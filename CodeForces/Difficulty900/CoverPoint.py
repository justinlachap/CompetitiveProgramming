# solution to https://codeforces.com/problemset/problem/1047/B

n = int(input())

coord = []
for i in range(n):
    x, y = map(int, input().split())
    coord.append(x + y)
print(max(coord))
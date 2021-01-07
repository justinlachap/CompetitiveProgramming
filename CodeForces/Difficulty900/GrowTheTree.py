# solution https://codeforces.com/problemset/problem/1248/B

n = int(input())

x = 0
y = 0

sticks = [int(x) for x in input().split()]

sticks.sort()

for i in range(n//2):
    x += sticks[i]

for j in range(n//2,n):
    y += sticks[j]

print(x**2 + y**2)
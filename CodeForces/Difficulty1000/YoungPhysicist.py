# solution to https://codeforces.com/problemset/problem/69/A

n = int(input())
forces = []

for i in range(n):
    force = input().split()
    forces.append(force)
    x, y, z = 0, 0, 0
    for j in forces:
        x += int(j[0])
        y += int(j[1])
        z += int(j[2])

if x == y == z == 0:
    print('YES')
else:
    print('NO')

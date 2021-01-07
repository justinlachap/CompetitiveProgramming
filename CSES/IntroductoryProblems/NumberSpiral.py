# solution https://cses.fi/problemset/task/1071

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    z = max(y, x)
    z_squared = (z - 1) * (z - 1)
    if z % 2 == 0:
        if y == z:
            print(z_squared + x)
        else:
            print(z_squared + 2 * z - y)
    else:
        if x == z:
            print(z_squared + y)
        else:
            print(z_squared + 2 * z - x)

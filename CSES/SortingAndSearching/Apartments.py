# solution https://cses.fi/problemset/task/1084/

n, m, k = map(int, input().split())
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
i, j, count = 0, 0, 0
while i < n and j < m:
    if a[i] + k < b[j]:
        i += 1
    elif a[i] - k > b[j]:
        j += 1
    else:
        i += 1
        j += 1
        count += 1
print(count)

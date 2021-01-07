# solution to https://codeforces.com/problemset/problem/58/A


hello = ['h','e','l','l','o']
index = 0

for i in input():
    if i == hello[index]:
        index += 1
        if index == 5:
            break

print('YES') if index == 5 else print('NO')
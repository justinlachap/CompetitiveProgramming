# solution to codeforces.com/problemset/problem/275/A

n = int(input())
total = 0
list = []

for i in input().split():
    total += int(i)
    list.append(int(i))

ways = 0
if total % 2 == False:
    for j in list:
        if j % 2 == False:
            ways += 1

elif total % 2 == True:
    for k in list:
        if k % 2 == True:
            ways += 1

print(ways)

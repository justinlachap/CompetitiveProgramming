#solution https://codeforces.com/problemset/problem/1520/A

t = int(input())

for i in range(t):
    n = int(input())
    tasks = input()
    count = 1
    for i in range(len(tasks)-1):
        if tasks[i] == tasks[i+1]:
            count += 1
            continue
        elif count != tasks.count(tasks[i]):
            print("NO")
            break
        else:
            count = 1
    else:
        print("YES")
# solution for https://codeforces.com/problemset/problem/149/A

k = int(input())

months = input().split()
months.sort(key=int,reverse=True)


cm, count = 0, 0

for i in months:
    if cm >= k:
        print(count)
        break
    else:
        cm += int(i)
        count += 1
        if cm >= k:
            print(count)
            break

if cm < k:
    print(-1)
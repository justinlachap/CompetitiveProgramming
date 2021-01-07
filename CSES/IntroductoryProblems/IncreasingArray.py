# solution https://cses.fi/problemset/task/1094

n = int(input())
array = [int(x) for x in input().split()]

count = 0
for i in range(1, len(array)):
    if array[i] < array[i - 1]:
        count += array[i - 1] - array[i]
        array[i] = array[i - 1]

print(count)
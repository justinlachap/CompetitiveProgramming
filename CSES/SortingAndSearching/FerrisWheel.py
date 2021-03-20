n, x = map(int, input().split())

weights = [int(x) for x in input().split()]

count = 0
gondolas = []

for i in weights:
    for j in range(len(gondolas)):
        if i + gondolas[j] <= x:
            gondolas[j] += i
            break
    else:
        if i <= x:
            gondolas.append(i)

print(len(gondolas))

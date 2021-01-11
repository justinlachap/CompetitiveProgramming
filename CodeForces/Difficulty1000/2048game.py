q = int(input())

for games in range(q):
    n = int(input())
    multiset = sorted([int(x) for x in input().split()])
    lenght = len(multiset)
    while True:
        if 2048 in multiset:
            break
        for i in range(len(multiset) - 1):
            if multiset[i] == multiset[i + 1]:
                multiset[i] += multiset[i]
                del multiset[i + 1]
                multiset.sort()
                break
        if len(multiset) < lenght:
            lenght = len(multiset)
        else:
            break
    print('YES') if 2048 in multiset else print('NO')

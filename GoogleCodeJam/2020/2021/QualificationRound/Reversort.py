t = int(input())

def reverse_sublist(lst,start,end):
    lst[start:end] = lst[start:end][::-1]
    return lst

for i in range(t):
    n = int(input())
    L = [int(j) for j in input().split()]
    cost = 0
    it = 0
    for k in range(n-1):
        min_value = None
        index = None
        for z in range(it, n):
            if not min_value:
                min_value = L[z]
                index = z
            elif L[z] < min_value:
                min_value = L[z]
                index = z

        cost += (index-it+1)
        L = reverse_sublist(L, it, index)
        index += 1
    print(cost)

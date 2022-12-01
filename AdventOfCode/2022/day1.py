arr1 = [[paragraph.split("\n")] for paragraph in (
    open('input.txt', 'r').read().split("\n\n"))]
arr2 = []

for item in arr1:
    for j in range(len(item[0])):
        if (item[0][j]).isnumeric():
            item[0][j] = int(item[0][j])
    try:
        arr2.append(sum(item[0]))
    except:
        pass

# Question 1
print(sorted(arr2)[-1:])
# Question 2
print(sum(sorted(arr2)[-3:]))
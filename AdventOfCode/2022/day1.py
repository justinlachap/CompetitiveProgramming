arr1 = [[paragraph.split("\n")] for paragraph in (
    open('input.txt', 'r').read().split("\n\n"))]
arr2 = []

for item in arr1:
    try:
        arr2.append(sum([int(x) for x in item[0] if x.isnumeric()]))
    except:
        pass

# Question 1
print(sorted(arr2)[-1:])
# Question 2
print(sum(sorted(arr2)[-3:]))

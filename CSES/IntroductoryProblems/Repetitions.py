# solution https://cses.fi/problemset/task/1069

DNA = input()
substrings = ['']

lenghts, index = [1], 0
for i in range(len(DNA) - 1):
    if DNA[i] == DNA[i + 1]:
        lenghts[index] += 1
    else:
        lenghts.append(1)
        index += 1

print(max(lenghts))

# This is another way I found but it's too slow

# for i in range(len(DNA) - 1):
#     substrings[index] += DNA[i]
#     if DNA[i] != DNA[i + 1]:
#         substrings.append('')
#         index += 1
#
# substrings[index] += DNA[len(DNA) - 1]
# print(max([len(j) for j in substrings]))

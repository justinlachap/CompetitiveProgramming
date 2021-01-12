t = int(input())

for i in range(t):
    s = [int(x) for x in input()]
    for j in range(len(s)):
        s[j] = ['(' for k in range(s[j])] + [s[j]] + [')' for l in range(s[j])]

    s = sum(s, [])
    indexes = []
    for m in range(len(s) - 1):
        if s[m] == ')' and s[m + 1] == '(':
            indexes.append(m)
            indexes.append(m + 1)
    for o in reversed(indexes):
        del s[o]
    s = [str(x) for x in s]
    print(f"Case #{i + 1}: " + "".join(s))

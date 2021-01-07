# solution to https://codeforces.com/problemset/problem/118/A

vowels = ['a','e','i','o','u','y']
l = ['']

for i in input().lower():
    if i not in vowels:
        l.append(i)

print(".".join(l))

# solution https://codeforces.com/problemset/problem/1428/C , time limit exceeded but its python you know...

t = int(input())


def concat(string, index):
    return string[2:len(string)] if index == 0 else string[:index] + string[index + 2:len(string)]


def string_shorten(string):
    for i in range(len(string) - 1):
        if (string[i] == string[i + 1] == 'B') or (string[i] == 'A' and string[i + 1] == 'B'):
            return concat(string, i)

    return False


for i in range(t):
    s = input()
    while string_shorten(s) != False:
        s = string_shorten(s)

    print(len(s))

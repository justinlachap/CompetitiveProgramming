# solution to https://codeforces.com/problemset/problem/122/A

lucky_numbers = [4, 7, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]

n = int(input())
answer = None

for i in lucky_numbers:
    if n % i == 0:
        answer = 'YES'
        break

print(answer) if answer == 'YES' else print('NO')

# solution https://cses.fi/problemset/task/1070

n = int(input())

# We know that if n = 2 or if n = 3, it's impossible to get a "beautiful" permutation. With any other natural number, we can put the even numbers in ascending order and then the odd numbers in ascending order.

if n == 2 or n == 3:
    print('NO SOLUTION')
else:
    permutation = sorted([x for x in range(1, n + 1)])
    output = [i for i in permutation if i % 2 == 0] + [j for j in permutation if j % 2 != 0]
    print(' '.join(str(k) for k in output))
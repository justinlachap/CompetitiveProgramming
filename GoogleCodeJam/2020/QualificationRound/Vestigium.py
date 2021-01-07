t = int(input())

for _ in range(t):
    N = int(input())
    M = []
    for i in range(N):
        M.append([int(x) for x in input().split()])
    trace = 0
    index = 0
    for i in range(len(M)):
        trace += M[i][index]
        index += 1

    rows = 0
    elements = []

    for i in range(len(M)):
        for j in range(0, N):
            if elements.count(M[i][j]) > 0:
                rows += 1
                break
            else:
                elements.append(M[i][j])
        elements.clear()

    colums = 0
    for i in range(len(M)):
        for j in range(0, N):
            if elements.count(M[j][i]) > 0:
                colums += 1
                break
            else:
                elements.append(M[j][i])
        elements.clear()

    print('Case #' + str(_ + 1) + ': ' + str(trace) + ' ' + str(rows) + ' ' + str(colums))

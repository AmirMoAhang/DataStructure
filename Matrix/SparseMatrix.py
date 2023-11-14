def sparseMatrix(sparce, n):
    arr = []
    count = 0
    arr.append([n, n, 0])
    for i in range(n):
        for j in range(n):
            if sparce[i][j] != 0:
                arr.append([i, j, sparce[i][j]])
                count += 1
    
    arr[0][2] = count
    return arr


# begin just for test
zart = sparseMatrix([
    [5, 0, 0, 10, 0, -5],
    [0, 12, 4, 0, 0, 0],
    [0, 0, 0, -8, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0, 0],
    [0, 0, 45, 0, 0, 0]
], 6)

for i in range(len(zart)):
    print(zart[i])

# end
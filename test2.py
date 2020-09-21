dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    matrix = []
    global wz
    global gz
    for j in range(n):
        matrix.append(list(input()))
        if 'S' in matrix[j]:
            wz = [j, matrix[j].index('S')]
        if 'E' in matrix[j]:
            gz = [j, matrix[j].index('E')]


    def hasPath(start, end):
        res = []
        for d in dd:
            new_x = start[0] + d[0]
            new_y = start[1] + d[1]
            if 0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] != '#' and path[new_x][new_y] == -1:
                path[new_x][new_y] = path[start[0]][start[1]] + 1
                res.append([new_x, new_y])

        return res
    path = [[-1] * m for i in range(n)]
    q = [wz]
    while q:
        cur_node = []
        for j in q:
            res = hasPath(j, path)
            cur_node += res
        q = cur_node
    if path[gz[0]][gz[1]] == -1:
        print('NO')
    else:
        print('YES')

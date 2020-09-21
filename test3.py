direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
t = int(input())
for _ in range(t):
    global prince, princess
    matrix = []
    n, m = map(int, input().split())
    for j in range(n):
        matrix.append(list(input()))
        if 'S' in matrix[-1]:
            prince = [j, matrix[-1].index('S')]
        if 'E' in matrix[-1]:
            princess = [j, matrix[-1].index('E')]


    def hasPath(start, visited):
        res = []
        for item in direction:
            new_x = start[0] + item[0]
            new_y = start[1] + item[1]
            if 0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] != '#' and visited[new_x][new_y] == -1:
                res.append([new_x, new_y])
                visited[new_x][new_y] = 0
        return res


    visited = [[-1] * m for i in range(n)]
    record = [prince]
    while record:
        tmp = []
        for item in record:
            res = hasPath(item, visited)
            tmp += res
        record = tmp
    if visited[princess[0]][princess[1]] == 0:
        print('YES')
    else:
        print('NO')

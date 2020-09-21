n, m = map(int, input().split())
people, station = [], []
for _ in range(n):
    people.append(list(map(int, input().split())))
for _ in range(m):
    station.append(list(map(int, input().split())))

min_dis = 0

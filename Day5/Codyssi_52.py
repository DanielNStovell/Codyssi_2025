with open("main.txt", 'r') as file:
  lines = [line.strip() for line in file.readlines()]

coords = []
for line in lines:
  coords.append(list(map(int, line.strip("()").split(","))))

visited = [[0,0]]
dis = []
def next(x, y):
  closest = [float('inf'), float('inf')]
  minDis = float('inf')
  for k in coords:
    if k not in visited:
      distancet = abs(x - k[0]) + abs(y - k[1])
      if (distancet < minDis or (distancet == minDis and k[0] < closest[0]) or (distancet == minDis and k[0] == closest[0] and k[1] < closest[1])):
        minDis = distancet
        closest = k
        
  dis.append(abs(visited[-1][0] - closest[0]) + abs(visited[-1][1] - closest[1]))
  visited.append(closest)

ans = 0

for i in range(len(coords)):
  next(visited[i][0], visited[i][1])
print(sum(dis))
print(visited)
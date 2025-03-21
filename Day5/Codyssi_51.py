with open("main.txt", 'r') as file:
  lines = [line.strip() for line in file.readlines()]

coords = []
for line in lines:
  coords.append(list(map(int, line.strip("()").split(","))))
print(coords)
distances = []

closest = [float('inf'), float('inf')]

for k in coords:
  distances.append(abs(k[0]) + abs(k[1]))
  if abs(k[0]) + abs(k[1]) < abs(closest[0]) + abs(closest[1]):
    closest = k

distances2 = []

print(closest)

for k in coords:
  if k != closest:
    distances2.append(abs(k[0] - closest[0]) + abs(k[1] - closest[1]))
print(distances2)
print(min(distances2))
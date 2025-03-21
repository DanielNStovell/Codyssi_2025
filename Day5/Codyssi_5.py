with open("main.txt", 'r') as file:
  lines = [line.strip() for line in file.readlines()]

coords = []
for line in lines:
  coords.append(list(map(int, line.strip("()").split(","))))
print(coords)
distances = []

for k in coords:
  distances.append(abs(k[0]) + abs(k[1]))

print(distances)
print(max(distances) - min(distances))
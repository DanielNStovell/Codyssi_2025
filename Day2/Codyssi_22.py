with open("Codyssi.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

rooms = list(map(int, lines[4:]))
print(rooms)

a = int(lines[0].split()[-1])
m = int(lines[1].split()[-1])
p = int(lines[2].split()[-1])

rooms.sort()
adf = []
for i in rooms:
  if i % 2 == 0:
    adf.append(i)

ans = sum(adf) ** p
ans *= m
ans += a

print(ans)

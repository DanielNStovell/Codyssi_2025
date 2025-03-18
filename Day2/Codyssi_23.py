with open("Codyssi.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

rooms = list(map(int, lines[4:]))
print(rooms)

a = int(lines[0].split()[-1])
m = int(lines[1].split()[-1])
p = int(lines[2].split()[-1])

rooms.sort()

max = -1
for i in rooms[::-1]:
  afk = (i**p) * m + a
  if afk <= 15000000000000:
    max = i
    break

print(max)

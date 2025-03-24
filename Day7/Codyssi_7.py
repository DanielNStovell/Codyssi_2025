with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

tracks = lines[0:lines.index("")]
swaps = lines[lines.index("")+1:-2]
ansIdx = lines[-1]

print(tracks)
print(swaps)
print(ansIdx)

for i in swaps:
  x, y = i.split("-")
  x, y = int(x)-1, int(y)-1
  tracks[x], tracks[y] = tracks[y], tracks[x]

print(tracks[int(ansIdx)-1])
with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

tracks = lines[0:lines.index("")]
swaps = lines[lines.index("")+1:-2]
ansIdx = lines[-1]

print(tracks)
print(swaps)
print(ansIdx)

for i in range(len(swaps)):
  x, y = swaps[i].split("-")
  if i != len(swaps)-1:
    z = swaps[i+1].split("-")[0]
  else:
    z = swaps[0].split("-")[0]
  x, y, z = int(x)-1, int(y)-1, int(z)-1

  tracks[x], tracks[y], tracks[z] = tracks[z], tracks[x], tracks[y]

print(tracks[int(ansIdx)-1])
with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

tracks = lines[0:lines.index("")]
swaps = lines[lines.index("")+1:-2]
ansIdx = lines[-1]

ordtrack = lines[0:lines.index("")]
ordtrack.sort()

print(tracks)
print(swaps)
print(ansIdx)

for i in range(len(swaps)):
  print(i, tracks)
  x, y = swaps[i].split("-")
  x, y = int(x)-1, int(y)-1

  if x > y: 
    x, y = y, x

  blcoklenx = min(len(tracks) - x, y - x)
  blocklen = min(len(tracks) - y, blcoklenx)

  for j in range(blocklen):
    print(j)
    tracks[x + j], tracks[y + j] = tracks[y + j], tracks[x + j]

print(tracks[int(ansIdx)-1])
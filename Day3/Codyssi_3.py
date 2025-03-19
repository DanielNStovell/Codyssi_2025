with open("Codyssi.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0
  
for line in lines:
  rangessss = line.split()
  print(rangessss)
  for range in rangessss:
    sstart, end = map(int, range.split('-'))
    ans += end - sstart + 1
    
print(ans)
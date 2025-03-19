with open("Codyssi.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0
  
for line in lines:
  rangessss = line.split()
  print(rangessss)
  uni = []
  
  for range1 in rangessss:
    sstart, end = map(int, range1.split('-'))
    print(sstart, end)

    for num in range(sstart, end + 1):
      if num not in uni:
        uni.append(num)

  ans += len(uni)

print(ans)
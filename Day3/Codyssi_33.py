with open("Codyssi.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0
adf = []

for line in lines:
  rangessss = line.split()
  uni = []
  
  for range1 in rangessss:
    sstart, end = map(int, range1.split('-'))

    for num in range(sstart, end + 1):
      if num not in uni:
        uni.append(num)

  adf.append(uni)   

print(adf)

maxu = 0

for i in range(len(adf) - 1):
  first = adf[i]
  next = adf[i + 1]
    
  for num in next:
    if num not in first:
      first.append(num)

    size = len(first)
    maxu = max(maxu, size)

print(ans)
print(maxu)
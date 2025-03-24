with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

total = 0
rar = []
for line in lines:
  temp = []
  for j in line:
    if temp != [] and ((temp[-1].isalpha()) and j.isdigit() or temp[-1].isdigit() and (j.isalpha())):
      temp = temp[:-1]
    else:
      temp.append(j)
  rar.append(temp)
for k in rar:
  total += len(k)
print(total)
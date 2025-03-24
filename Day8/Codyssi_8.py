with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

total = 0
for line in lines:
  for j in line:
    if j.isalpha():
      total += 1
print(total)
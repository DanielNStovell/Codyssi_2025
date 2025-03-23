with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

total = 0
for i in lines[0]:
  if i.isalpha():
    total += 1
print(total)
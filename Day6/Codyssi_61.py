with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

total = 0
for i in lines[0]:
  if i.isalpha():
    if i.lower() == i:
      total += ord(i) - ord('a') + 1
    else:
      total += ord(i) - ord('A') + 27
print(total)
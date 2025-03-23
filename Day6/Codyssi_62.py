with open("main.txt", "r") as file:
  lines = [line.strip() for line in file]

total = 0
def calc(num):
  while num < 1:
    num += 52
  while num > 52:
    num -= 52
  return num

for i in lines[0]:
  if i.isalpha():
    if i.lower() == i:
      temp = ord(i) - ord('a') + 1
    else:
      temp = ord(i) - ord('A') + 27
  else:
    temp = calc(lastval * 2 - 5)

  lastval = temp
  total += temp

print(total)
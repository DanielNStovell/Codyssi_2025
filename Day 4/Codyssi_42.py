with open("Codysii.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0
data = []

for line in lines:
  seq = ""
  last = line[0]
  count = 1
  for idx in range(1, len(line)):
    if line[idx] == line[idx-1]:
      count += 1
    else:
      seq += f"{count}{line[idx-1]}"
      count = 1
  seq += f"{count}{line[idx-1]}"
  data.append(seq)

print(data)

for line in data:
  num = 0
  for letter in line:
    if letter.isdigit():
      num += int(letter)
    else:
      num += (ord(letter) - ord('A')) + 1
  print(num)
  ans += num

print(ans)
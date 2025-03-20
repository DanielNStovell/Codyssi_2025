with open("Codysii.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0
data = []

for line in lines:
  char = len(line) // 10
  data.append(f"{line[:char]}{len(line)-2*char}{line[-char:]}")
print(data)
for line in data:
  for letter in line:
    if letter.isdigit():
      ans += int(letter)
    else:
      ans += (ord(letter) - ord('A')) + 1

print(ans)
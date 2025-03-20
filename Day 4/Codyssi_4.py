with open("Codysii.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

ans = 0

for line in lines:
  for letter in line:
    ans += (ord(letter) - ord('A')) + 1

print(ans)
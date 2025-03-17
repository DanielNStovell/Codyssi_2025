with open("Codyssi.txt", 'r') as file:
  lines = [line.strip() for line in file.readlines()]

print(lines)

d = int(lines[0] + lines[1])
print(d)

for i in range(2, len(lines)):  
  try:
    int(lines[i])
  except:
    c = [int(lines[j] + lines[j+1]) for j in range(2, i, 2)]
    sym = lines[i]
    print(sym)

print(c)
sym = sym[::-1]
print(sym)
ans = d

for i in range(len(c)):  
  if sym[i] == '+':  
    ans += c[i]  
  else:  
    ans -= c[i]

print(ans)

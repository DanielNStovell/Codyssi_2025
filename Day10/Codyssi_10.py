with open("main.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

grid = [list(map(int, line.split())) for line in lines]

rows = [row for row in grid]
cols = []

for r in range(len(grid)):
  tmep = []
  for c in range(len(grid[0])):
    tmep.append(grid[c][r])
  cols.append(tmep)
print(cols)

row_sum = [sum(row) for row in rows]
col_sum = [sum(col) for col in cols]
print(min(min(row_sum), min(col_sum)))
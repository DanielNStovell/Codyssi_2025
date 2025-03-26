with open("main.txt", "r") as file:
  lines = [line.strip() for line in file.readlines()]

grid = [list(map(int, line.split())) for line in lines]

dp = [[0] * len(grid[0]) for i in range(len(grid))]
dp[0][0] = grid[0][0]

for row in range(1, len(grid)):
  left = dp[row - 1][0]
  dp[row][0] = left + grid[row][0]

for col in range(1, len(grid[0])):
  up = dp[0][col - 1]
  dp[0][col] = up + grid[0][col]


for row in range(1, len(grid)):
  for col in range(1, len(grid[0])):
    left = dp[row][col - 1]
    up = dp[row - 1][col]
    dp[row][col] = min(left, up) + grid[row][col]

ans = dp[14][14]

print(ans)
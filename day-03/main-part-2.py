import re

TEST=True
TEST=False

def load_grid():
  if TEST:
    file = "input-sample.txt"
  else:
    file = "input.txt"

  print("Loading ", file)
  rows = []
  with open(file) as f:
    while line := f.readline():
      line = line.strip()
      print(line)
      rows.append(line)
  return rows

def load_cogs(grid):
  out = []
  for i, row in enumerate(grid):
    for m in re.finditer('\*', row):
      out.append((i, m.start()))
  print("Cogs:", out)
  return out

def load_numbers(grid):
  out = []
  for i, row in enumerate(grid):
    for m in re.finditer(r'\d+', row):
      out.append((int(m.group()), i, m.start(), m.end()))
  print("Numbers:", out)
  return out

def cog_is_connected_to_number(cog, number):
  row = cog[0]
  offset = cog[1]

  cells = [
    (row - 1, offset - 1),
    (row - 1, offset),
    (row - 1, offset + 1),
    (row, offset - 1),
    (row, offset + 1),
    (row + 1, offset - 1),
    (row + 1, offset),
    (row + 1, offset + 1)
  ]

  number_row = number[1]
  number_from = number[2]
  number_to = number[3]

  for cell in cells:
    cell_row = cell[0]
    cell_col = cell[1]
    if cell_row == number_row and cell_col >= number_from and cell_col < number_to:
      return True

  return False

def connections_for_cog(cog):
  out = [number[0] for number in numbers if cog_is_connected_to_number(cog, number)]
  print("Connections for", cog, ":", out)
  return out

grid = load_grid()
numbers = load_numbers(grid)
cogs = load_cogs(grid)

total = 0
for cog in cogs:
  connections = connections_for_cog(cog)
  if len(connections) > 1:
    x = 1
    for connection in connections:
      x = x * connection
    total += x




print("Total:", total)
if TEST:
  print("Expected:", 467835)

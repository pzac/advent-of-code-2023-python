import re

TEST=True
TEST=False

class Schematic:
  def __init__(self, file):
    self.rows = []
    row = 0
    with open(file) as f:
      while line := f.readline():
        self.rows.append(Row(row, line.strip()))
        row += 1
    self.width = len(self.rows[0].data)
    self.height = len(self.rows)


  def total_sum(self):
    tot = 0
    for c in self.components():
      tot += c.value
    return tot

  def components(self):
    return [item for item in self.items() if self.is_valid(item)]

  def items(self):
    out = []
    for row in self.rows:
      for item in row.extract_numbers():
        out.append(Item(row.number, item))
    return out

  def is_valid(self, item):
    for offset in range(item.start, item.end):
      if self.cell_next_to_symbol(item.row_number, offset):
        return True
    return False

  def cell_next_to_symbol(self, row, offset):
    cells = []
    cells.append((row - 1, offset - 1))
    cells.append((row - 1, offset))
    cells.append((row - 1, offset + 1))
    cells.append((row, offset - 1))
    cells.append((row, offset + 1))
    cells.append((row + 1, offset - 1))
    cells.append((row + 1, offset))
    cells.append((row + 1, offset + 1))

    values = [self.value_for(cell[0], cell[1]) for cell in cells]

    items = [x for x in values if x is not None]
    for i in items:
      if i not in '1234567890.':
        return True
    return False

  def value_for(self, row, offset):
    if row < 0 or row >= self.height or offset < 0 or offset >= self.width:
      return None
    return self.rows[row].data[offset]

  def inspect(self):
    print("Schematic")
    for row in self.rows:
      row.inspect()

class Item:
  def __init__(self, row_number, tuple):
    self.row_number = row_number
    self.value = tuple[0]
    self.start = tuple[1]
    self.end = tuple[2]

class Row:
  def __init__(self, number, data):
    self.number = number
    self.data = data

  def inspect(self):
    print("Row", self.number, self.data, self.extract_numbers())

  def extract_numbers(self):
    return [(int(m.group()), m.start(), m.end()) for m in re.finditer(r'\d+', self.data)]

def main():
  if TEST:
    file = "input-sample.txt"
  else:
    file = "input.txt"

  print("Loading ", file)

  schematic = Schematic(file)

  schematic.inspect()

  total_sum = schematic.total_sum()

  print("Total sum:", total_sum)
  if TEST:
    expected = 4361
    if total_sum == expected:
      print("CORRECT!!")
    else:
      print("WRONG!! Should be", expected)


if __name__ == "__main__": main()

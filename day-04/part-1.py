import sys
import re

rows = sys.stdin.readlines()
# print(rows)

def extract_numbers(data):
  return [int(m.group()) for m in re.finditer(r'\d+', data)]

items = []
for row in rows:
  _label, data = row.split(":")
  left, right = data.split("|")
  items.append(
    [extract_numbers(left), extract_numbers(right)]
  )

total = 0

for x, y in items:
  matches = [i for i in x if i in y]
  num_matches = len(matches)
  if num_matches > 0:
    points = 2 ** (num_matches - 1)
    total += points

print("Total", total)

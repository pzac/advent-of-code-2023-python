file = "input.txt"

print(file)

def extract_numbers(string):
  return [c for c in string if c >= '0' and c <= '9']


sum = 0

with open(file) as f:
  while line := f.readline():
    line = line.rstrip()
    print(line)
    numbers = extract_numbers(line)
    print(numbers)
    a, b = numbers[0], numbers[-1]

    sum += int(a+b)

print("total ", sum)

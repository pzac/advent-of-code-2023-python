file = "input-sample.txt"
file = "input.txt"

NUMBERS = {
  "one" : 1,
  "two" : 2,
  "three" : 3,
  "four" : 4,
  "five" : 5,
  "six" : 6,
  "seven" : 7,
  "eight" : 8,
  "nine" : 9
}

print(file)

def replace_strings(string, reverse=False):
  if reverse:
    string = flip_string(string)

  copy = string
  for s, _i in ordered_numbers_as_strings(string, reverse=reverse):
    if reverse:
      digit = NUMBERS[flip_string(s)]
    else:
      digit = NUMBERS[s]
    copy = copy.replace(s, str(digit))
  return copy


def ordered_numbers_as_strings(string, reverse=False):
  out = []
  for s, i in NUMBERS.items():
    if reverse:
      s = flip_string(s)
    pos = string.find(s)
    if pos != -1:
      out.append((s, pos))
  return sorted(out, key=lambda item: item[1])

def extract_first_number(string):
  return [c for c in string if c > '0' and c <= '9'][0]

def first_number(string):
  converted = replace_strings(string)
  return extract_first_number(converted)

def last_number(string):
  converted = replace_strings(string, reverse=True)
  return extract_first_number(converted)

def flip_string(string):
  return ''.join(reversed(string))


sum = 0

with open(file) as f:
  while line := f.readline():
    line = line.rstrip()
    a = first_number(line)
    b = last_number(line)
    sum += int(a+b)

print("total ", sum)

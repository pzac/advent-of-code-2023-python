FILE = "input-sample.txt"
FILE = "input.txt"

MAX = {
  'red': 12,
  'green': 13,
  'blue': 14
}


class Game:
  def __init__(self, data):
    game, sets = data.split(":")
    _, game_id = game.split(" ")
    self.game_id = int(game_id)

    self.sets = [Set(x) for x in sets.split(";")]

  def is_valid(self):
    for set in self.sets:
      if not set.is_valid():
        return False
    return True

  def power(self):
    min = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    for set in self.sets:
      for color, num in set.colors.items():
        if min[color] < num:
          min[color] = num
    return min['red'] * min['green'] * min['blue']

class Set:
  def __init__(self, data):
    self.data = data
    self.colors = {}
    tokens = data.split(",")
    for t in tokens:
      num, col = t.strip().split(' ')
      self.colors[col] = int(num)

  def is_valid(self):
    for color, num in self.colors.items():
      if num > MAX[color]:
        return False
    return True


sum = 0
power_sum = 0


with open(FILE) as f:
  games = []
  while line := f.readline():
    line = line.rstrip()
    games.append(Game(line))


for game in games:
  if game.is_valid():
    sum += game.game_id
  power_sum += game.power()

print("game id sum:", sum)
print("power sum:", power_sum)

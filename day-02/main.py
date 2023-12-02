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


with open(FILE) as f:
  games = []
  while line := f.readline():
    line = line.rstrip()
    games.append(Game(line))


for game in games:
  if game.is_valid():
    sum += game.game_id

print(sum)

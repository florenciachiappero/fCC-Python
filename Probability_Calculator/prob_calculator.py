import copy
import random


class Hat:
  
  def __init__(self, **kwargs):
    contents = []
    for key in kwargs.keys():
      for _ in range(kwargs[key]):
        contents.append(key)
    self.contents = contents
    

  def draw(self, amount):

    if amount >= len(self.contents):
      return self.contents

    sample = []

    for _ in range(amount):
      index = random.randrange(len(self.contents))
      ball = self.contents[index]
      sample.append(ball)
      self.contents = self.contents[0:index] + self.contents[index + 1:]
    return sample



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for _ in range(num_experiments):
    example = copy.copy(hat)
    sample = example.draw(num_balls_drawn)
    success = True
    for key in expected_balls.keys():
      if sample.count(key) < expected_balls[key]:
        success = False
        break
    if success:
      count += 1

  return count / num_experiments
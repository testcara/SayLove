import random

class SayLove(object):
    def __init__(self):
      with open('love_quotes') as love_file:
        self.data = love_file.readlines()

    def say(self):
      print(random.choices(self.data)[0].strip("\n"))


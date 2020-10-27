import random
class Dice():
    def __init__(self, crooked=False):
        self.is_crooked = crooked

    def throw(self):
        while True:
            num = random.randint(1,6)
            if self.is_crooked and num % 2:
                continue
            return num

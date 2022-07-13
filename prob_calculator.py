import copy
import random

class Hat:
    # Initialize hat class and prepare information in a usefull way
    def __init__(self, **colors):
        self.contents = []
        for color, num in colors.items():
            for _ in range(num):
                self.contents.append(color)
    
    # Draw the number of given balls
    def draw(self, draws):
        if draws > len(self.contents):
            drawn = copy.copy(self.contents)
            self.contents.clear()
            return drawn
        drawn = []
        for _ in range(draws):
            drawn.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return drawn


# Make experiment run a given number of times, we will record all successful runs in num_of_occurrences and we can therefore calculate Successes/Total
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_of_occurrences = 0
    for _ in range(num_experiments):
        at_least_as_many = True
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        for color, num in expected_balls.items():
            if drawn.count(color) < num:
                at_least_as_many = False
                break
        if at_least_as_many:
            num_of_occurrences += 1
    return num_of_occurrences / num_experiments


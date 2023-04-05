import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_move, y_move):
        self.x = self.x + x_move
        self.y = self.y + y_move

    def length(self, point2):
        leng = ((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5
        return round(leng, 2)

class RedButton:
    def __int__(self):


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))

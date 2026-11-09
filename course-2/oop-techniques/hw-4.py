class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def on_x_axis(self):
        if self.y == 0: return True
        else: return False



print(news)
print(news.get_name())
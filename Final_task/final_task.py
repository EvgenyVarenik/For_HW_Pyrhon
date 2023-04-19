class Dragon:
    def __init__(self, height, danger, color):
        self.height = height 
        self.danger = danger
        self.color = color
 
    def __lt__(self, other):
        return self.height < other.height and self.danger < other.danger and self.color < other.color
 
    def __le__(self, other):
        return self.height <= other.height and self.danger <= other.danger and self.color <= other.color
 
    def __gt__(self, other):
        return self.height > other.height and self.danger > other.danger and self.color > other.color
 
    def __ge__(self, other):
        return self.height >= other.height and self.danger >= other.danger and self.color >= other.color
 
    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color
 
    def __ne__(self, other):
        return self.height != other.height or self.danger != other.danger or self.color != other.color
 
    def __add__(self, other):
        new_color = self.color if self.color < other.color else other.color
        new_height = (self.height + other.height) // 2
        new_danger = self.danger if self.danger > other.danger else other.danger
        return Dragon(height=new_height, danger=new_danger, color=new_color)
 
    def __isub__(self, value):
        self.height -= self.height // value
        self.danger += self.danger % value
        return self
 
    def __mod__(self, value):
        new_height = self.height % value
        new_danger = self.danger // value
        new_color = self.color
        return [Dragon(new_height, new_danger, new_color) for _ in range(value)]
 
    def __call__(self, string):
        return string * self.danger
 
    def change_color(self, color):
        if self.danger > 1:
            self.danger -= 1
            self.color = color
        else:
            self.color == color
 
    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.danger} and color {self.color}'
 
    def __repr__(self):
        return f'{self.height}, {self.danger}, {self.color}'
    
dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")
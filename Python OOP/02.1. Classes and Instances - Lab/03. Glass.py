class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        self.content += ml

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        space_left = 0
        return f'{space_left} ml left'


# Test code:

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

# Expected output:

# Glass filled with 100 ml
# Cannot add 200 ml
# Glass is now empty
# Glass filled with 200 ml
# 50 ml left


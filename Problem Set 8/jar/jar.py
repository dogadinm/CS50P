
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative")
        self.volume = capacity
        self.cookies = 0


    def __str__(self):
        return "🍪" * self.cookies


    def deposit(self, n):
        if self.cookies + n > self.volume:
            raise ValueError("Too many cookies.")
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("You can't take more cookies.")
        self.cookies -= n

    @property
    def capacity(self):
         return self.volume

    @property
    def size(self):
        return self.cookies

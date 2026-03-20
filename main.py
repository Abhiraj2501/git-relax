print("hello world")
def add(a, b):
    return a + b

print(add(2, 3))

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
l = [1, 2, 3]
print(type(l))
l.append(4)
string_ = 'str'
print(type(string_))

class Exemplo():
    pass

x = Exemplo()

print(type(x))

class Dog:
    def __init__(self):
        self.idade = 10

dog = Dog()
dog2 = Dog()
print(dog.idade)
print(dog2.idade)
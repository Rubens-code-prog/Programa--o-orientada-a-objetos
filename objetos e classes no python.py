l = [1, 2, 3]
#print(type(l))
l.append(4)
string_ = 'str'
#print(type(string_))

class Exemplo():
    pass

x = Exemplo()

#print(type(x))

class Dog:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
        #print(f'{raca} criado')
    
    def envelhecer(self):
        self.idade += 1
        return self.idade

dog = Dog('Labrador')
dog2 = Dog('Huskie')
dog.idade = 11
dog.envelhecer()
#print(dog.idade)
#print(dog.raca)
#print(dog2.idade)
#print(dog2.raca)

class circle:
    def __init__(self, raio=1):
        self.raio = raio
    
    def calcula_area(self):
        return self.raio * self.raio * 3.14
    
    def retorna_raio(self):
        return self.raio

c1 = circle()
c2 = circle(2)
# print(c1.retorna_raio())
# print(c2.retorna_raio())

#HERANÇA
class animal():
    def __init__(self):
        print("animal criado")

    def quem_sou_eu(self):
        print('eu sou um animal')
    
    def comer(self):
        print('comendo')

class cachorro(animal):
    def __init__(self):
        animal.__init__()
        print('eu sou um cachorro')

    def quem_sou_eu(self):
        print('eu sou um cachorro')

animal = animal()
animal.quem_sou_eu()

dog = cachorro()
dog.quem_sou_eu()
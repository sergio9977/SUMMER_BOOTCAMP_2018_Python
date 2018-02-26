"""
Las variables de clase son para atributos y métodos compartidos
por todas las instancias de la clase.
Las variables de instancia son para datos únicos para cada instancia

El diseño correcto de la clase debería
usar una variable de instancia
"""

class Dog:

    kind = 'canine'         # class variable

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)               # shared by all dogs
print(e.kind)               # shared by all dogs

print(d.name)               # unique to d
print(e.name)               # unique to e



class Dog2:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d2 = Dog2('Fido')
e2 = Dog2('Buddy')
d2.add_trick('roll over')
e2.add_trick('play dead')

print(d2.tricks)            # unexpectedly shared by all dogs

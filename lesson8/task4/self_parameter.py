"""
self es el primer parámetro que se pasa a cualquier método de clase.
Python usará el parámetro self para referirse al objeto que se está creando.
"""
class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0
    def add(self, amount):
        instans = Calculator()
        instans.current += amount
        return instans.current

    def get_current(self):
        instans = Calculator()
        return instans.current

# Para Complex cree el objeto y realize una llamada al metodo

clase1 = Complex()
clase1.create(4,7)

# Para Calculator cree el objeto y realize llamadas a los metodos
# identifique y resuelva el problema

ClaseCalcu = Calculator()
print(ClaseCalcu.add(7))
print(ClaseCalcu.get_current())

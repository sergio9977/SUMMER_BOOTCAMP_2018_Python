"""
Un objeto combina variables y funciones en una sola entidad.
Los objetos obtienen sus variables y funciones de las clases.
Las clases son esencialmente plantillas para crear tus objetos.
Se puede pensar en un objeto como una única estructura de datos
que contiene datos y funciones.
Las funciones de los objetos se llaman métodos.

la variable "my_object" contiene un objeto
de la clase "MyClass" que contiene la variable y la función "foo"
"""
class MyClass:
    variable = 12

    def foo(self):
        print("Hello from function foo")

my_object = MyClass()

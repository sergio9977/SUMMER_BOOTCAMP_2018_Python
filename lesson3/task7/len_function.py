"""
La función len() se usa para contar cuántos caracteres contiene una cadena.
obtener la primera mitad de la frase
"""
phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
print(first_half)

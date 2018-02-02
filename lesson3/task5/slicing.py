"""
Slicing se usa para obtener varios caracteres (una subcadena) de una cadena.
Su sintaxis es similar a la de indexación, pero en lugar de solo un índice,
utiliza dos índices (números) separados por dos puntos
Ej. str[ind1:ind2]

str[inicio:fin] # elementos comienzan hasta el final-1
str[inicio:]    # elementos comienzan por el resto de la matriz
str[: end]      # elementos desde el principio hasta el final-1
str[:]          # una copia completa

"""
monty_python = "Monty_Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:12] # (P-6)(n-11) Python
print(python)

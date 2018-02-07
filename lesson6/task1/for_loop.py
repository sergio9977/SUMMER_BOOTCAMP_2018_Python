"""
los loops se utilizan para iterar sobre una secuencia dada.
En cada iteración, la variable definida en el ciclo for se asignará
al siguiente valor en la lista.
El tipo de range representa una secuencia de números inmutable
https://docs.python.org/3/library/stdtypes.html#typesseq-range
"""

for i in range(5):    # range(5) retorna 0, 1, 2, 3, 4
    print(i)

primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)


f = open("C:/Users/Sergio/Documents/PythonCurso/SUMMER_BOOTCAMP_2018_Python/lesson10/task1/input.txt", "r")

for line in f.readlines():
    print(line)

f.close()

f1 = open("C:/Users/Sergio/Documents/PythonCurso/SUMMER_BOOTCAMP_2018_Python/lesson10/task1/input1.txt", "r")

print(f1.readline())

f1.close()

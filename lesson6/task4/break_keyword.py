count = 0

while True:
    print(count)
    count += 1
    if count == 5:
        break


zoo = ["lion", 'tiger', 'elephant']
while True:
    animal = zoo.pop()
    print(animal)
    if animal is 'tiger':
        break

import random

file = open('dab.ppm', 'w')

file.write("P3 \n1000 1000 \n255\n")
for i in range(1000000):
    file.write(str(random.randint(0, 255)) + " " + str(random.randint(0, 255)) + " " + str(random.randint(0, 255)) + " ")

file.close()

import random

file = open('dab.ppm', 'w')

file.write("P3 \n1000 1000 \n255\n")
for i in range(1000):
    for j in range(1000):
        file.write(str(i*j % 255) + " " + str(i*j%255) + " " + str(i*j%255) + " ")

file.close()

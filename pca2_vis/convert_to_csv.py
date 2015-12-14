import numpy as np
import itertools


parsed = []
with open('pca2_5pops.txt') as f:
	for line in f:
		line = line.split(',')
		x = float(line[1][1:])
		y = float(line[2][:len(line[2])-3])
		pop = line[0][1:]
		parsed.append((pop, x, y))

f = open("pca2_5pops.csv", "w")
f.write("pop,x_coord,y_coord" + "\n")
for i in range(len(parsed)):
    f.write(parsed[i][0] + "," + str(parsed[i][1])+ "," + str(parsed[i][2]) +"\n")
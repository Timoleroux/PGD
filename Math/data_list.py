from math import *  
from random import randint

values = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
sorted_values = values.sort()

# -------- ALL DATA --------

# Max
max = sorted_values[-1]

# Min
min = sorted_values[0]

# Range
range = max - min

# Sum of values
sum_values = 0
for i in values:
    sum_values += i

# Mean
mean = 0
for i in values:
    mean += i
    mean /= sum_values


# Standard deviation and variance
std_dev = 0
for i in values:
    std_dev += (int(values[i]['val']) - mean)*(int(values[i]['val']) - mean)
std_dev /= sum_nbr
variance = std_dev
std_dev = sqrt(int(std_dev))



# Display all the informations
for i in values:
    print("Value :", values[i]['val'], "| Number :", values[i]['nbr'])
print("-----------------------")
print("Number of data points :", len(values))
print("Minimum :", min)
print("Maxmium :", max)
print("Range :", range)
print("Sum of values", sum_values)
print("Mean :", round(mean, 2))
print("Standard deviation :", round(std_dev, 2))
print("Variance :", round(variance, 2))


# Afficher des graphiques plt dans une fenêtre pySide


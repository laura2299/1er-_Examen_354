# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:43:25 2023

@author: Leidy
"""
import csv
import random


# Se carga el conjunto de datos desde un archivo CSV
with open('C:/Users/WINDOWS 11/Documents/ds_salaries.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Se mezcla el conjunto de datos
random.shuffle(data)

# Se obtiene el índice de división
N = len(data)
print(N)
n_test = N // 5 #el 20% de N
n_train = N - n_test # el 80% de N

#se generan dos listas una para train y otra para test
train_indices = list(range(n_train))
test_indices = list(range(n_train, N))

#se pueden usar estas listas para acceder a los datos correspondientes
#en el conjunto de datos
train_data = [data[i] for i in train_indices]
test_data = [data[i] for i in test_indices]

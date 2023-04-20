# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:43:25 2023

@author: WINDOWS 11
"""
import csv
import random

# Se define la proporción de entrenamiento y prueba
train_prop = 0.8
test_prop = 0.2

# Se carga el conjunto de datos desde un archivo CSV
with open('C:/Users/WINDOWS 11/Documents/ds_salaries.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Se mezcla el conjunto de datos
random.shuffle(data)

# Se obtiene el índice de división
n = len(data)
train_idx = round(train_prop * n)

# Se divide el conjunto de datos
train = data[:train_idx]
test = data[train_idx:]


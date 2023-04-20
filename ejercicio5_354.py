# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:40:48 2023

@author: WINDOWS 11
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Cargar el dataset
dataset = pd.read_csv('C:/Users/WINDOWS 11/Documents/ds_salaries.csv')



# Tomar un subconjunto aleatorio de 4 columnas y 20 filas
columnas_seleccionadas = ['experience_level', 'salary', 'salary_currency', 'salary_in_usd']
filas_seleccionadas = np.random.choice(dataset.index, size=20, replace=False)
dataset_s = dataset.loc[filas_seleccionadas, columnas_seleccionadas]

# Crear una columna de etiquetas para el árbol de decisión 
etiquetas = np.random.choice([0, 1], size=20)
print("etiquetas: ",etiquetas)
# Realizar la codificación de variables categóricas a numéricas
dataset_s_encoded = pd.get_dummies(dataset_s)
print(dataset_s_encoded)
# Crear y ajustar el modelo de árbol de decisión
modelo_arbol = DecisionTreeClassifier(criterion='entropy', splitter='best')
modelo_arbol.fit(dataset_s_encoded, etiquetas)

# Graficar el árbol de decisión
fig = plt.figure(figsize=(10, 8))
_ = tree.plot_tree(modelo_arbol, 
                   feature_names=dataset_s_encoded.columns, 
                   class_names=['0', '1'],
                   filled=True)
plt.show()

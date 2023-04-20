# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:06:46 2023

@author: laura
"""

#3. Del dataset anterior realice en PYTHON, tres algoritmos de preprocesamiento. Explique la razón de aplicar estas técnicas.

#1Eliminación de duplicados:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import LabelEncoder

# Cargar el dataset
df = pd.read_csv('C:/Users/WINDOWS 11/Documents/ds_salaries.csv')

print("Dataset antes de la binarización:")
print(df)

# Eliminar duplicados basados en todas las columnas
dff = df.drop_duplicates()
print("dataset eliminando duplicados")
print(dff)
#explicacion los dataset pueden contener duplcados lo que puede alterar el
#resulado esperado estimado,La elimminacion de duplicadfos es una tecnoca que 
#permite identificar filas duplicadas y asi asegurar la integridad de los datos
print("--------------------------------------------")
#2 La discretización de variables numéricas

# Seleccionar la columna numérica a discretizar
columna_numerica = dff['salary_in_usd']
print("columna numerica:")
print(columna_numerica)
# Definir los intervalos para la discretización
intervalos = [5132, 49618, 94105, 138592, 183079, 227566,272052,316539,450000]

# Aplicar la discretización
columna_discretizada = pd.cut(columna_numerica, bins=intervalos, labels=False, right=False)

# Mostrar los resultados
print("columna discretizada")
print(columna_discretizada)

#explicacion la discretizacion de variables numericas es una tecnica de 
#preprocesamiento que consta en dividir una variable numerica en una variable catergorica
#o intervalos, esto puede resultar util en casos como la construccion de 
#modelos de aprendizaje automatico que requieren var categoricas como entrada
print("--------------------------------------------")
#3 LabelEncoder Codificacion dde variables categoricas en representaciones numericas
columna_categorica=dff['experience_level']
print("columna categorica nivel de experiencia: SE,Mi,EN,EX")
print(columna_categorica)

# Crear una instancia del LabelEncoder
le = LabelEncoder()
# Ajustar y transformar la variable categórica
columna_codificado = le.fit_transform(columna_categorica)
# Mostrar los resultados
print("Variable codificada: ")
print( columna_codificado)

#explcacion: al contrario que es anterior algoritmo, este convierte las 
#varibles categoricas en numericas 



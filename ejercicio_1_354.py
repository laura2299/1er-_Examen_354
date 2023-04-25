
import pandas as pd
import matplotlib.pyplot as plt

print("-----------------Media moda, percentil sin LIBRERIAS---------------------)

from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir("/content/drive/MyDrive/datos")
dataframe = pd.read_csv("ds_salaries.csv")
print(dataframe)
print("---------PERCENTIL 90----------")
# 1: Ordenar los datos por la columna 'salary'

datos_ordenados = sorted(dataframe['salary'])
print(datos_ordenados)
#  2: Calcular el rango intercuartil 
Q1 = datos_ordenados[int(len(datos_ordenados)*0.25)]
Q3 = datos_ordenados[int(len(datos_ordenados)*0.75)]
IQR = Q3 - Q1

# 3: Calcular el porcentaje de datos que se encuentran por debajo del percentil 90
p = (len(datos_ordenados)-1)*0.9 + 1

# 4: Interpolar el valor del percentil 90 en los datos ordenados
if p % 1 == 0:
    # Si el porcentaje es un número entero, el percentil corresponde a un valor en los datos ordenados
    P = datos_ordenados[int(p)-1]
else:
    # Si el porcentaje no es un número entero, se interpola el valor
    i = int(p) - 1
    d = p % 1
    P = datos_ordenados[i] + d * (datos_ordenados[i+1] - datos_ordenados[i])


print("El percentil 90 de la columna 'salary' es:", P) 
print("................MEDIA..................")
import numpy as np
# Definimos la columna que queremos calcular la media
datos = dataframe['salary']
print(datos)

# Calculamos la suma de los valores en la columna
suma = np.int64(0)
for elemento in datos:
    suma =suma + elemento
# Calculamos el número total de valores en la columna
num_valores = len(datos)

# Calculamos la media de los valores en la columna
media = suma / num_valores
print("La media de la columna es:", media)
print("---------------------------Media de una variable categorica------------------")
from sklearn.preprocessing import LabelEncoder
columna_me = dataframe['experience_level']
print(columna_me)
le = LabelEncoder()
# Ajustar y transformar la variable categórica
columna_codificada = le.fit_transform(columna_me)
# Mostrar los resultados
print("Variable codificada: ")
print( columna_codificada)
suma = np.int64(0)
for elemento in columna_codificada:
    suma =suma + elemento
num_valores = len(columna_codificada)

media2 = suma / num_valores
print("La media de la columna categorica es:", media2)
#Moda de la columna salary
print("----------------MODA-------------------------")
columna = dataframe['salary'].tolist()
frecuencias = {}
for valor in columna:
    if valor not in frecuencias:
        frecuencias[valor] = 1
    else:
        frecuencias[valor] += 1


moda = None
frecuencia_maxima = 0
for valor, frecuencia in frecuencias.items():
    if frecuencia > frecuencia_maxima:
        moda = valor
        frecuencia_maxima = frecuencia

print('La moda de la columna es:', moda)


print(".......moda de una variable categorica................")

columna = dataframe['experience_level']
print(columna)
le = LabelEncoder()
# Ajustar y transformar la variable categórica
columna_codificado = le.fit_transform(columna)
# Mostrar los resultados
print("Variable codificada: ")
print( columna_codificado)

frecuencias = {}
for valor in columna_codificado:
    if valor not in frecuencias:
        frecuencias[valor] = 1
    else:
        frecuencias[valor] += 1


moda = None
frecuencia_maxima = 0
for valor, frecuencia in frecuencias.items():
    if frecuencia > frecuencia_maxima:
        moda = valor
        frecuencia_maxima = frecuencia

print('La moda de la columna es:', moda)

      
      
print("-------------------------MEDIA,MODA,PERCENTIL CON LIBRERIAS----------------------------------)     
print("------------Media con libreria pandas--------------------------")
media_por_columna = dataframe.mean()
print(media_por_columna)
print("------------Moda con libreria pandas--------------------------")
moda_por_columna = dataframe.mode()
print(moda_por_columna)

print("------------cuartiles con libreria pandas--------------------------")

cuartiles_por_columna = dataframe.quantile([0.25, 0.5, 0.75])
print(cuartiles_por_columna) 
print("------------percentiles con libreria pandas--------------------------")
percentiles_por_columna = dataframe.quantile([0.1, 0.25, 0.5, 0.75, 0.9])
print(percentiles_por_columna)


plt.plot(dataframe['work_year'], dataframe['experience_level'], 'ro')
plt.xlabel('Etiqueta del eje X')
plt.ylabel('Etiqueta del eje Y')
plt.title('Título del gráfico')
plt.show()
#En el primer grafico podemos ver que en cada año tenemos una cantidad x de cada nivel de experiencia del empleado.

plt.plot(dataframe['employee_residence'], dataframe['company_location'], 'ro')
plt.xlabel('Etiqueta del eje X')
plt.ylabel('Etiqueta del eje Y')
plt.title('Título del gráfico')
plt.show()

#Para las columnas residencia de empleado y ubicacion de la compañia se puede ver 
#que tenemos una linea que va hacia arriba 
#lo que significa que la mayoria de los valores se corresponden segun la lista de datos.






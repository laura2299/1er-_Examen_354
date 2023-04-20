

import pandas as pd


#Media de columna 1
#De la columna años contamos la cantidad por años y luego le sacamos la media de esas cantiddes:
def media_columna1(columna):
    cont1 = columna.count(2023)
    cont2 = columna.count(2022)
    cont3 = columna.count(2021)
    cont4 = columna.count(2020)
    suma = cont1+cont2+cont3+cont4
    media= suma/4
    return media
    
def media_2(columna):
     cont1 = columna.count('SE')
     cont2 = columna.count('MI')
     suma = cont1+cont2
     media= suma/2
     return media

    
def media_salario(columna):
    suma = 0
    for num in columna:
        suma += num

    # Calcular la media dividiendo la suma entre el número de elementos
    media = suma / len(columna)
    return media
# Abrir el archivo CSV con pandas
from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir("/content/drive/MyDrive/datos")
dataframe = pd.read_csv("ds_salaries.csv")


# Obtener los datos de la primera columna en una lista
columna1 = dataframe.iloc[:, 0].tolist()
# Imprimir la lista
print("Contenido de la primera columna en 'micolumna':")
print(columna1)
#aplicar la media a esta columna
media1= media_columna1(columna1)
print("la media de la col:",media1)
#media de columna2 El nivel de experiencia en el trabajo durante el año


columna2 = dataframe.iloc[:, 1].tolist()

media2=media_2(columna2)
print("La media de columna 2 es:",media2)
#Media Columna 3

#media de columna 5 salario
columna5 = dataframe.iloc[:, 4].tolist()
print("la columna de salarios:")
print(columna5)
media5= media_salario(columna5)
print("La media de salarios es :",media5)

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



















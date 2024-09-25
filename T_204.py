# Ej1. Mediante teclado especificar los siguiente:
# - Numero de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe

import pandas as pd
import numpy as np
from numpy.ma.core import append

valor1 = input("Introduce el número de columnas: ")
valor2 = input("Introduce el número de filas: ")
list1 = []
list2 = []

for idx in range(0,int(valor1)):
   string1 = str(idx)
   string2 = "Introduce el nombres de la columna "+ string1 + ": "
   valor3 = input(string2)
   list1.append(valor3)

for idx in range(0,int(valor2)):
   string3 = str(idx)
   string4 = "Introduce el nombres de la fila "+ string3 + ": "
   valor4 = input(string4)
   list2.append(valor4)

print(list1)
print(list2)

array = np.random.uniform(-10, 10, size= [int(valor1),int(valor2)])

print(array)

df = pd.DataFrame(array, list1, list2)

print(df)
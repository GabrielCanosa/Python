# Series

# Ejemplo 1
import pandas as pd

serie1 = pd.Series([5,10,15])
print(serie1[1])

# Ejemplo 2
asignaturas = ['Matemáticas','Fisica','Quimica','Historia','Geografía','Literatura']
notas = [10,6,8,5,7,5]

serie_notas_alumno = pd.Series(notas, index = asignaturas)

print(serie_notas_alumno['Quimica'])
print(serie_notas_alumno[serie_notas_alumno >= 8])

# Convertir serie en diccioario
diccionario = serie_notas_alumno.to_dict()
print(diccionario)

# Convertir diccioario en serie
serie_notas_alumno2 = pd.Series(diccionario)


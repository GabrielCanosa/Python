# Manejo de excepciones

try:
  result = 2 / 0
  print(result)
except ZeroDivisionError:
  print("No es posible dividir por cero")
except:
  print("Ha ocurrido un error")
else:
  print("todo correcto")
finally:
  print("Esta prueba ha finalizado")

# Expresiones regulares
import re

texto = "Lorem impsum dolor sit amet"

encontrado = re.search("dolor", texto)

if(encontrado): print("se encontro")
else: print("no se encontro")

re.split("ipsum", texto) # ["Lorem ", " dolor sit amet"]

re.sub("sit", "abcdefg", texto) # Lorem impsum dolor abcdefg amet"

#############################
#           JSON
#############################
# Convertimos un diccionario en json
import json
producto1 = {"nombre": "silla", "color": "blanco", "precio": 20 }

yeison = json.dumps(producto1)

# Convertimos un json en un diccionario
diccionario = json.loads(yeison)


# Fecha y hora

from datetime import datetime

fechayhora = datetime.now()

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

hora = fechayhora.hour
minuto = fechayhora.minute
segundo = fechayhora.second

# Crear base de datos
import sqlite3
conexion = sqlite3.connect("BaseDeDatos.db")

# Crear tabla
cursor = conexion.cursor()
cursor.execute("CREATE TABLE Personas(id INT NOT NULL, nombre VARCHAR(30) NOT NULL)")

conexion.commit()
conexion.close()
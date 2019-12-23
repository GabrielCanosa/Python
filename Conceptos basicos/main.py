"""
Esto es una introduccion a Python, los conceptos básicos. Variables, condicionales, bucles, clases, funciones, etc
"""
# Variables
cadena = "Hola mundo";
print(cadena);

numero1 = 4;
numero2 = 3;
print(numero1 + numero2);

numeroDecimal = 3.1416
print(numero2 + numeroDecimal); # Permite sumar numeros enteros y decimales

# Conversiones de tipos de datos
cadenaNumero1 = str(numero1);
numero3 = int("8");
print(numero1 + numero3);

# Cadenas de texto
print(cadena[0]); # H
print(cadena[1:7]);
print(len(cadena));
print(cadena.upper());
print(cadena.split());

nombre = "Gabriel"
edad = 30;
print("Hola {}, feliz {} cumpleaños".format(nombre, edad));
print(f"Hola {nombre}, feliz {edad} cumpleaños");

resultado = 10/3;
print("Resultado = {r:1.3f}".format(r=resultado));

# Entrada por teclado
print("Escriba su nombre");
entrada = input();
print("Hola " + entrada);

# Operadores aritmeticos

numero4 = 5;
numero5 = 2;
print(numero4 + numero5);
print(numero4 - numero5);
print(numero4 / numero5);
print(numero4 * numero5);
print(numero4 % numero5);
print(numero4 ** 3); # 5 al cubo

# Operadores de asignacion
numero6 = 6;
print(numero6);
numero6 += 2;
print(numero6);
numero6 -= 2;
print(numero6);
numero6 *= 2;
print(numero6);
numero6 /= 2;
print(numero6);
numero6 **= 2;
print(numero6);

# Operadores de comparacion

"""
== iguales
!= diferentes
> mayor a
< menor a
>= mayor o igual
<= menor o igual
"""

# Operadores logicos
# and or not

print(numero5 > numero6);
print(not(numero5 > numero6));

print(numero5 > numero6 and numero4 > numero6);
print(numero5 > numero6 or numero4 > numero6);

# Operadores de identidad
# is , is not

frutas = ["manzana", "banana"];
frutas2 = ["manzana", "banana"];
frutas3 = frutas;

print(frutas3 is frutas);
print(frutas3 is frutas2);
print(frutas3 is not frutas2);

# Operadores de pertenencia
# in, not in

manzana = "manzana";
pera = "pera";

print(manzana in frutas);
print(pera in frutas);
print(pera not in frutas);

# Listas

colores = ["rojo", "azul", "amarillo", "verde"];
print(colores);
colores[1] = "violeta";
print(colores);
print(len(colores));
colores.append("blanco");
print(colores)
colores.remove("amarillo");
print(colores)
colores.clear();
print(colores)

# Tuplas
tuplaColores = ("rojo", "azul");
# tuplaColores.remove("rojo");
# salta un error por que no se puede modificar

# Diccionarios
ciudades = {1: "Madrid", 2:"Valencia", 3:"Barcelona"};
print(ciudades[2]);
ciudades[4] = "Malaga";
print(ciudades);
ciudades.pop(3);
print(ciudades);

# Condiciones
num1 = 10;
if(num1 < 5): print("es menor que 5");
elif(num1 > 15): print("es mayor a 15");
else: print("esta entre 5 y 15");

# Bucle for
paises = ["España", "Italia", "Francia", "Holanda", "Portugal", "Inglaterra"];
for pais in paises:
  if(pais == "Francia"): continue;
  print(pais);
  if(pais == "Portugal"): break;

# Bucle while
num2 = 15;
while(num1 < num2):
  print(num1);
  num1 += 1;

# Clases y objetos
class Silla:
  color = "blanco"
  precio = 100

silla = Silla();
print(f"la silla de color {silla.color} cuesta {silla.precio} $")

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def saludar(self):
    print("Hola, me llamo {} tengo {} años".format(self.nombre, self.edad))

persona1 = Persona("Juan", 37)
persona1.saludar()

def despedir():
  print("Sayonara... baby")

despedir()

def Sumar(num1, num2):
  return num1 + num2

print(Sumar(4,8));

# Funciones lambda

resultado = lambda num : num + 30

print(resultado(10))

resultado2 = lambda num_1 , num_2 : num_1 + num_2

print(resultado2(3,5))

# Modulos

# 1 archivo llamado modulo1.py
"""
def funcionDelModulo1():
  print("hace algo");

def funcionDelModulo2():
  print("hace algo");
"""
# Otro archivo, que llama al fichero modulo1.py y ejecuta la funcion funcionDelModulo de esta forma:
"""
# importo todo el modulo

import modulo1 
modulo1.funcionDelModulo();

# o puedo importar solo la funcion que necesito

from modulo1 import funcionDelModulo2
modulo1.funcionDelModulo2();

# y se le cambia el nombre diciendo:

from modulo1 import funcionDelModulo2 as funcion2
modulo1.funcion2();

"""

# leer ficheros de texto
# Se crea un archivo .txt llamado achivo1 con algo de texto
# y se lee de la siguiente forma
"""
fichero = open("nombreDelFichero.txt", "rt")
"""
# r = read, t = text
"""
contenidoFichero = fichero.read()
print(contenidoFichero);
"""

# Grabar ficheros

ficherowt = open("ficheroParaGrabar.txt", "wt")
# crea un fichero llamado ficheroParaGrabar.txt y lo abre en modo
# w = escritura, t = texto

ficherowt.write("Estoy es el texto que voy a grabar en el fichero ficheroParaGrabar.txt")

ficherowt.close()


#Añadir info a un fichero de texto ya existente

fichero = open("ficheroExistente", "at")
# a = append, t = text
fichero.write("\nIncluimos esta cadena de texto en un fichero que ya tiene cosas escritas")

fichero.close()

# Borrar un fichero
import os

os.remove("nombreDelFicheroParaBorrar.txt")
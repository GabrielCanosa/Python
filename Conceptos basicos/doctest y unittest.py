# Doctest - Pruebas dentro de la documentacion
def Sumar(numero1, numero2):
  """
  Documentacion de la funcion Sumar.
  Recibe dos numero como parametro y devuelve su suma.
  >>> Sumar(1,2)
  3
  """
  return numero1 + numero2

resultado = Sumar(3,4)

print(resultado)

import doctest
doctest.testmod()

#Se ejecuta en la terminal: python nombreArchivo.py -v

# Unittest - Pruebas dentro del codigo

def  Multiplicar(num1, num2):
  return num1*num2

res = Multiplicar(4,5)
print(res)

import unittest

class Pruebas(unittest.TestCase):
  def Test(self):
    self.assertEqual(Multiplicar(4,2),8)

if __name__ == '__name__':
  unittest.main()

#Se ejecuta en la terminal: python nombreArchivo.py
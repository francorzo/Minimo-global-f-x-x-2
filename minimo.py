import math
import sys 
def biseccion(x1,x2):
   x3=1
   while evalf(x3) > 0.0002 or evalf(x3) < -.0002:
      x3=(x1+x2)/2
      if evalf(x3) * evalf(x1) > 0:
         x1=x3
      else:
         x2=x3
   return x3

def evalf(x):
   f = 2 * x
   return f

print ("Ingrese el valor del primer punto")
x1=input()
print ("Ingrese el valor del segundo punto")
x2=input()

if evalf(x1)*evalf(x2)>0:
   print("No se puede determinar un minimo")
else: 
   minimo=biseccion(x1,x2) 
   print "El minimo es = ", minimo



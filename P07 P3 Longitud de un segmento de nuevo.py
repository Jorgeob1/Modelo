import math
def potencia(x,n):

  poten=1

  for i in range(0,n):

    poten=poten*x
    

  return poten


def longitud(x1,y1,x2,y2):
  distancia=math.sqrt(potencia(x2-x1,2) + (potencia(y2-y1,2)))
  return distancia


x1=int(input("primera variable x"))
y1=int(input("primera variable y"))
x2=int(input("segunda variable x"))
y2=int(input("segunda variable y"))
aa=longitud(x1,y1,x2,y2)
print(aa)
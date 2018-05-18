def potencia(x,n):

  poten=1

  for i in range(0,n):

    poten=poten*x
    

  return poten
n=int(input("numero entero"))
x=int(input("variable y"))
aa=potencia(x,n)
print(aa)














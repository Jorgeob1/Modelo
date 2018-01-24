A=int(input("primer numero entero"))
B=int(input("segundo numero enteros"))
if(A<B):
  for c in range(A, B+1):
    print(c)
else:
  if(A>B):
   for i in range(A, B-1,-1):
    print(i)
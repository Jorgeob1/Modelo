a=int(input("primer numero entero"))
b=int(input("segundo numero entero"))
c=int(input("tercer numero entero"))
if (a==b==c):
  print(3)
elif ((a==b)or(a==c)or(b==c)):
   print(2)
#asi tambien vale   
#elif ((a!=b)or(a!=b)or(b!=c)):
#   print(0)
else : 
  print(0)

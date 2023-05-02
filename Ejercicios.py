#for i in [1,2,3,4,5]:
#  print(i)

#for i in ["Maria","Juan","Pedro","Carmen","Carlos"]:
#  print(i)

#print(list(range(2, 10)))
#print(list(range(0, 3)))
#print(list(range(2,10,2)))
#print(list(range(2,10,3)))
#print(list(range(10,5,-1)))
#print(list(range(3,-1,-1)))
#print(list(range(10,1,-3)))
#print(list(range(2,5,1)))
#print(list(range(2,5)))
#print(list(range(10)))

#print("con while")
#x=0
#while (x<10):
#  print(x)
#  x+=1


#print("con for")
#for x in range(10):
#  print(x)

'''
num= int(input("Ingrese un número a mostrar su table de multiplicar: "))
for x in range(15):
  print(x,"x",num,"es: ",x*num)

###
suma = 0
for i in range (1, 101):
  suma += i
print ("La suma es: ",suma)

###

n = int(input("Ingrese el número n: "))
m = int(input("Ingrese el número m: "))
if n<m:
  suma = 0
  for i in range (n,m+1):
    suma += i
  print(suma)
else:
  print("n debe ser menor a m")


###Otra forma: ###
n = int(input("n: "))
m = int(input("m: "))
if n<m:
  s= 0
  for x in range (n,m+1):
    s=s+x
  print(s)
else:
  print("Valores ingresados no válidos")

###Con while
n = int(input("n: "))
m = int(input("m: "))
while n>m:
  n = int(input("n: "))
  m = int(input("m: "))

s=0
for x in range (n,m+1):
  s=s+x
print(s)


##Comando: break
for x in range(10, 1, -1):
  if x>=5:
    print(x)
  else:
    break

##Comando: continue
for x in range(10):
  if x!=5:
    print(x)
  else:
    continue

'''

numero = int(input("ingrese un número entero: "))
primo = 1
for i in range (2, numero):
  if numero % i == 0:
    primo = 0
  if primo == 1:
    print("El número ", numero, " es primo")
  else:
    print("El número ", numero, " NO es primo")
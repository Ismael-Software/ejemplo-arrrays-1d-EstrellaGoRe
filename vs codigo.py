n=int(input("¿Cuántos números quieres ingresar? "))
v=[]
for i in range(n):
  num=int(input(f"Ingrese el número (i+1): "))
  v.append(num)
pos=0
ac=0
while pos< len(v):
    ac=ac + v[pos]
    pos=pos+ 1
    mayor=v[0]
for num in v:
  if num > mayor:
   mayor=num

print("Los números ingresados son:",v)
print("La sumatoria es:", ac)
print("El número mayor es:", mayor)

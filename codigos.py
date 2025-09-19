numero= int(input("ingresar el valor a factorizar "))
if numero < 0:
  print("no se puede factorizar un numero negativo")
else:
  factorial= 1
  for i in range(2, numero + 1):
    factorial *= i
    print(factorial)
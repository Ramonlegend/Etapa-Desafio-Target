def fibonacci(numero):
  a, b = 0, 1
  while b < numero:
    a, b = b, a + b
  if b == numero:
    return True
  else:
    return False

numero = int(input("Digite um numero: "))
if fibonacci(numero):
  print(f"{numero} pertence a sequencia de fibonacci.")
else:
  print(f"{numero} não pertence a sequencia de fibonacci.")


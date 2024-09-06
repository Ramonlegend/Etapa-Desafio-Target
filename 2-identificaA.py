def contar_letra_a(string):
  count = 0
  for char in string:
    if char.lower() == 'a':
      count += 1
  return count

string = input("Digite uma palavra: ")
quantidade = contar_letra_a(string)
print(f"A letra 'a' ocorre {quantidade} vezes na string.")
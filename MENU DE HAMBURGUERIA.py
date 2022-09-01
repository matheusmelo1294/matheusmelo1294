print("MENU DE HAMBURGUERIA")

print("\n")

print("1 - HAMBURGUER SIMPLES")
print("2 - X-BACON")
print("3 - HOT DOG")
print("4 - X-FRANGO")
print("5 - DUPLO CHEDDAR")

print("\n")
n = 0
while n == 0:
  sandwich = int(input("Digite o sanduíche que deseja consumir: "))
  if(sandwich == 1):
    print("HAMBURGUER SIMPLES")
    break
  elif(sandwich == 2):
    print("X-BACON")
    break
  elif(sandwich == 3):
    print("HOTDOG")
    break
  elif(sandwich == 4):
    print("X-FRANGO")
    break
  elif(sandwich == 5):
    print("DUPLO CHEDDAR")
    break
  else:
    print("Ops!! Não temos essa opção, tente novamente!")
print("\n")

drink = int(input("Deseja alguma bebida? Digite 1 para SIM e 2 para NÃO: "))

if(drink == 1):
  print("SIM")
  print("\n")
  print("****ESCOLHA SUA BEBIDA****")
  print("\n")
  print("1 - REFRI LATA")
  print("2 - COCA-COLA 2L")
  print("3 - GUARANÁ 2L")
  n = 0
  while n == 0:
    bebida = int(input("DIGITE O NÚMERO DA BEBIDA: "))
    if(bebida == 1):
      print("REFRI LATA")
      break
    elif(bebida == 2):
      print("COCA-COLA 2L")
      break
    elif(bebida == 3):
      print("GUARANÁ 2L")
      break
    else:
      print("Opa! Não temos essa opção!")
elif(drink == 2):
  print("NÃO")
  print("\n")

  print("Agora vamos ao cadastro!")

  print("\n")

adress = input("ENDEREÇO: ")
print("\n")

print(adress)

print("\n")

print("Como vai ser a forma de pagamento? ")

print("\n")

print("1 - PIX")
print("2 - CARTÃO")
print("3 - DINHEIRO")

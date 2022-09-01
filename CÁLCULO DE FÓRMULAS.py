print("***FÓRMULAS DE FÍSICA***")

print("\n")

name = input("NOME: ")

print('\n')

print(name, 'olá, tudo bem? Vamos calcular!! Escolha a fórmula na qual deseja efetuar')

print("\n")

print("1 - VELOCIDADE MÉDIA")
print("2 - ACELERAÇÃO MÉDIA")
print("3 - ENERGIA CINÉTICA")
print("4 - ENERGIA POTENCIAL GRAVITACIONAL")
print("5 - IMPULSO")

print("\n")

n = 0
while n == 0:
  formula = int(input("Digite o número da disciplina que você queira calcular: "))
  if(formula == 1):
    print("VELOCIDADE MÉDIA")
    print("\n")
    desl = float(input("DESLOCAMENTO (METROS): "))
    print(desl, "metros")
    tempo = float(input("TEMPO (SEGUNDOS): "))
    print(tempo, 'segundos')
    vel = desl/tempo
    print('VELOCIDADE MÉDIA')
    print('\n')
    print(vel,'m/s')
    print("\n")

  elif(formula == 2):
    print("ACELERAÇÃO MÉDIA")
    print("\n")
    ve = float(input("VELOCIDADE (METROS POR SEGUNDO): "))
    print(ve, 'metros por segundo')
    time = float(input("TEMPO (SEGUNDOS): "))
    print(time, 'segundos')
    acel = ve/time
    print("ACELERAÇÃO MÉDIA")
    print("\n")
    print(acel, 'metros por segundo ao quadrado')
    print("\n")

  elif(formula == 3):
    print('ENERGIA CINÉTICA')
    print("\n")
    massa = float(input("MASSA (KG): "))
    print(massa, 'kg')
    speed = float(input("VELOCIDADE (METROS POR SEGUNDO): "))
    energiacine = (massa*speed*speed)/2
    print(energiacine, 'joules')
    print("\n")
          
  elif(formula == 4):
    print("ENERGIA POTENCIAL GRAVITACIONAL")
    print("\n")
    masss = float(input('MASSA (KG): '))
    print(masss, 'kg')
    altura = float(input("ALTURA (METROS): "))
    print(altura, 'metros')
    epg = masss*altura*9.81
    print(epg, "joules")
    print("\n")

  elif(formula == 5):
    print("IMPULSO")
    print("\n")
    forca = float(input("FORÇA (NEWTON): "))
    print(forca, 'N')
    tiempo = float(input("TEMPO (SEGUNDOS): "))
    print(tiempo, 'segundos')
    impulso = forca*tiempo
    print("\n")
    print(impulso, 'Ns')
    print("\n")
  else:
    print("Ops! Não temos essa opção!")
    print("\n")
    

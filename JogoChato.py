import random

print ("DESARME A BOMBA!\nA cada rodada será mostrado na tela 3 números (0 - 9) aleatórios, tente digita-los na ordem "
       "correta antes da bomba explodir")

num = (random.sample(range(0,9), 4))
print(f"Os números são : {num}\nCOMEÇOU, DESARME A BOMBA!")

senhaCerta = ''
for i in range(len(num)):
    i = random.choice(num)
    senhaCerta += str(i)
    num.remove(i)
    #  print(num)
#  print(senhaCerta)

senha = input("Senha: ")
cont = 0
while senha != senhaCerta:
    cont += 1
    print(cont)
    print("pi...")
    senha = input("Senha: ")
    if cont == 4:
        print('BOOOOM!\nVocê Perdeu.')
        break
else:
    print("PARABÉNS, VOCÊ DESRMOU A BOMBA!")
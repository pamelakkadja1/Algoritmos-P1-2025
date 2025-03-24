h=float(input("Digite a sua altura :"))
g=input("Digite seu genero:")
pesoidealM = (72.7*h)-58
pesoidealF= (62.1*h)-44.7
if(g=="m" or g=="M"):
    print(pesoidealM)
elif(g=="f" or g=="F"):
    print(pesoidealF)
else:
    print("Não é possivel fazer o calculo a partir do seu genero")
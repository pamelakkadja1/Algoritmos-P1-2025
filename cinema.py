idade= int(input("Digite sua idade :"))
acompanhado= input("Voce esta acompanhado ? (s/n)")
if(idade>=18 or acompanhado=="s"):
    print("Voce pode assistir o filme a vontade!")
else:
    print("Voce não pode assistir o filme! MUITO VIOLENTO!")
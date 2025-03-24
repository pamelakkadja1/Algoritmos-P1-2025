clienteNovo= input("Voce é cliente novo ? (s/n)")
valor= float(input("Qual o valor total das compras:"))
if(clienteNovo=="s" and valor>50):
    desconto=valor*0.1
    print(f"O seu desconto é {desconto}")
else:
    print("Voce não ganhou desconto...")
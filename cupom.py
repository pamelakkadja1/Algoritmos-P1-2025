Cupom=input('Digite seu cupom:')
valordacompra= float(input("Digite o valor da compra :"))
if(Cupom=="CUPOM20" and valordacompra>200):
    desconto=valordacompra*0.2
    print(f"Sua compra deu  {valordacompra}")
    print(f"Seu desconto foi de {desconto}")
    valorfinal=valordacompra-desconto
    print(f"Voce tem que pagar {valorfinal}")
else:
    print("Infelizmente voce não tem desconto.")
#As notas disponiveis serao de as de 1,5,10,50 e 100 reais

valor=float(input("Digite o valor do saque :"))

saida1=""
saida5=""
saida10=""
saida50=""
saida100=""

if(valor>=10 and valor <=600):
    if(valor>=100):
     notasCem=valor//100
     valor=valor%100
     print(f"Sacou {notasCem} nota(s) de cem")
    if(valor>=50):
      notasCinquenta=valor//50
      valor=valor%50
      print(f"Sacou {notasCinquenta} nota(s) de cinquenta")
    if(valor>=10):
        notasDez=valor//10
        valor=valor%10
        print(f"Sacou {notasDez} nota(s) de dez")
    if(valor>=5):
        notasCinco=valor//5
        valor=valor%5
        print(f"Sacou {notasCinco} nota(s) de cinco")
    if(valor>1):
        notasUm=valor//1
        valor=valor%1
        print(f"Sacou {valor} nota(s) de um")
else:
    print("O valor precisa entre 10 e 600")

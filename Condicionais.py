pontos = int (input ("Digite qual a pontuação atual :"))
acertou = input ("Digite 'a' se tiver acertado")
if(acertou=='a'):
    print("Voce acertou e ganhou 10 pontos")
    pontos = pontos + 10

numero = int (input("Digite um numero :"))
if(numero>10):
    print ("O numero que voce digitou é maior que 10")
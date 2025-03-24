#chaves
chaveporta=input ("Voce possui a chave da porta?(s/n)")
chavecadeado= input("Voce possui a chave do cadeado ? (s/n)")
alguememcasa=input("Tem alguem em casa? (s/n)")
if((chaveporta=="s" and chavecadeado=="s") or alguememcasa=="s"):
    print("Voce pode entrar na sua casa")
else:
    print("VAI DORMIR NA RUA!!")

from brute_lib import *
import time

file = open("C:\\Users\\Darkenar94\\Desktop\\brute_force (test)\\diz.txt", "r")
dizionario = file.read()
file.close()

lista_stringhe = pulisci(dizionario)
lista_combinazioni = [["numero", "parola", "numero"], 
["numero", "numero", "parola"], ["numero", "parola", "parola"], 
["parola", "numero", "parola"], ["parola", "parola", "numero"], 
["parola", "numero", "numero"]]

pwd = ""
password = ""
caratteri = 5

testate = []

in_esecuzione = True
while in_esecuzione:
    caratteri += 1
    if not caratteri > 20:
        for i in range(100): # 100 parole per test
            pwd = ""
            pwd = test_casaccio(caratteri, lista_stringhe, pwd, testate)
            print(pwd)
            if accesso(pwd):
                password = pwd
                in_esecuzione = False
            parole = test_ragionevole(lista_combinazioni, caratteri, lista_stringhe, "")
            for parola in parole:
                if not parola in testate:
                    testate.append(parola)
                    pwd = parola
                    print(pwd)
                    if accesso(pwd):
                        password = pwd
                        in_esecuzione = False
    else:
        caratteri = 5
        
print("\npassword: " + password)
input()

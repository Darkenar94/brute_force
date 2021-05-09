
from brute_lib import *
import time, os

file = open(os.path.join(os.getcwd(), "diz.txt"), "r")
dizionario = file.read()
file.close()

lista_stringhe = pulisci(dizionario)
lista_combinazioni = [["numero", "parola", "numero"],
["numero", "numero", "parola"], ["numero", "parola", "parola"],
["parola", "numero", "parola"], ["parola", "parola", "numero"],
["parola", "numero", "numero"]]

password = ""
minimo_caratteri = 5
massimo_caratteri = 20
operazione_in_corso = "cracking...\n"
operazione_effettuata = "password craccata.\n"

in_esecuzione = True
while in_esecuzione:
    minimo_caratteri += 1
    if not minimo_caratteri > massimo_caratteri:
        for i in range(100):
            pwd = test_casaccio(minimo_caratteri, lista_stringhe, "")
            mostra_interfaccia(pwd, massimo_caratteri, operazione_in_corso)
            #print(pwd)
            if accesso(pwd):
                password = pwd
                in_esecuzione = False
            lista_pwds = test_ragionevole(lista_combinazioni, minimo_caratteri, lista_stringhe, "")
            for pwd in lista_pwds:
                mostra_interfaccia(pwd, massimo_caratteri, operazione_in_corso)
                #print(pwd)
                if accesso(pwd):
                    password = pwd
                    in_esecuzione = False
    else:
        minimo_caratteri = 5

mostra_interfaccia(password, massimo_caratteri, operazione_effettuata)
input()

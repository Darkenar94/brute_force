
import random, os

def ridimensiona_finestra():
    os.system('mode con: cols=114 lines=26')

def mostra_interfaccia(password, tot_caratteri, parola):
    ridimensiona_finestra()
    print("\n"*8)
    print(" "*41 + "> " + parola)
    print(" "*44 + "+" + "-" *(tot_caratteri +2) + "+")
    print(" "*44 + "|", password + " "*(tot_caratteri - len(password)), "|")
    print(" "*44 + "+" + "-" *(tot_caratteri +2) + "+")

def accesso(password):
    return "LorenzoVit24" == password

def pulisci(stringa):
    return stringa.split("\n")

def aggiungi(pwd, parole_testate, caratteri, dizionario):
    if not pwd in parole_testate:
        parole_testate.append(pwd)
    else:
        pwd = ""
        return test_casaccio(caratteri, dizionario, pwd, parole_testate)

def test_casaccio(caratteri, dizionario, pwd, parole_testate):
    while not len(pwd) == caratteri:
        stringa = random.choice(dizionario)
        if not len(pwd) + len(stringa) > caratteri:
            pwd += stringa
    aggiungi(pwd, parole_testate, caratteri, dizionario)
    return pwd

def ottieni_parole(dizionario):
    parole = []
    for stringa in dizionario:
        if len(stringa) > 1:
            if not stringa in parole:
                parole.append(stringa)
    return parole

def spezza_parola(parole):
    parola = random.choice(parole)
    return random.choice([parola[0:len(parola)//2], parola[len(parola)//2:]])

def elabora_parole(dizionario):
    parole = ottieni_parole(dizionario)
    parola_intera = random.choice(parole)
    parola_spezzata = spezza_parola(parole)
    parole_elaborate = (parola_intera, parola_spezzata)
    return parole_elaborate

def controlla(possibile_parola, pwd, caratteri):
    if not len(pwd) + len(possibile_parola) > caratteri:
        pwd += random.choice([possibile_parola.lower(), possibile_parola.title()])
    else:
        pwd = "errore"
    return pwd

def aggiungi_parola(dizionario, pwd, caratteri):
    parola_intera, parola_spezzata = elabora_parole(dizionario)
    parola = random.choice([parola_intera, parola_spezzata])
    nuova_parola = controlla(parola, pwd, caratteri)
    if not nuova_parola == "errore":
        return nuova_parola
    return pwd

def ottieni_numeri(dizionario):
    numeri = []
    for stringa in dizionario:
        try:
            int(stringa)
        except:
            pass
        else:
            numeri.append(stringa)
    return numeri

def aggiungi_numero(dizionario, pwd, caratteri):
    lista_numeri = ottieni_numeri(dizionario)
    stringa = ""
    for i in range(random.choice([1, 2, 3, 4, 5, 6])):
        stringa += random.choice(lista_numeri)
    if not len(pwd) + len(stringa) > caratteri:
        pwd += stringa
    return pwd

def test_ragionevole(combinazioni, caratteri, dizionario, pwd):
    lista_parole = []
    while not len(lista_parole) == len(combinazioni):
        for combinazione in combinazioni:
            pwd = ""
            for i in range(len(combinazione)):
                if combinazione[i] == "parola":
                    pwd = aggiungi_parola(dizionario, pwd, caratteri)
                    continue
                pwd = aggiungi_numero(dizionario, pwd, caratteri)
            lista_parole.append(pwd)
    return lista_parole

##Cosa fa questo programma:

Il programma in questione genera delle parole con il fine di trovare la password impostata di default.
#
#Funzionamento del programma:
Il programma genera delle parole di una lunghezza compresa tra i 6 ed i 20 caratteri (con possibilità di modificarne i valori da codice), la lunghezza della parola che verrà generata è inizialmente impostata a 6 caratteri cercando di generare un totale di 100 parole per il primo test e 600 per il secondo ogni qual volta la lunghezza della parola verrà incrementata al termine dei 100 loop impostati di default (con possibilità di aumentarne il valore da codice). Al raggiungimento della lunghezza massima di 20 caratteri il valore verrà ripristinato a 6 ripetendo le operazioni effettuate fin quando non avrà generato la parola corrispondente alla password impostata di default.
#
#Funzionamento per test:
Il primo test che viene effettuato cerca di mischiare in maniera totalmente casuale le parole contenute in un file di testo, mentre il secondo esegue fondamentalmente la stessa operazione ma con un senso logico e seguendo quindi le diverse combinazioni prestabilite. Inoltre durante questa fase ha la possibilità di scegliere se utilizzare solo una parte della parola o la stessa ma per intero e di impostare la prima lettera in maiuscolo o di impostare la parola scelta in minuscolo incrementando le possibilità di riuscita, entrambi con il fine di trovare la password impostata di default.

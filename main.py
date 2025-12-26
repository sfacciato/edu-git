# Obiettivo: mostrare concetti di base (variabili, liste, ciclo, file).


# Importiamo il modulo random per scegliere elementi a caso
import random

# Creiamo una lista con tutti i caratteri possibili della password
caratteri = [
    'a','b','c','d','e','f','g','h','i','j',
    'A','B','C','D','E','F','G','H','I','J',
    '0','1','2','3','4','5','6','7','8','9',
    '!','@','#','$','%','&','*'
]

# Definiamo la lunghezza della password
lunghezza = 8

# Creiamo una stringa vuota che conterrà la password
password = ""

# Ripetiamo l'operazione 8 volte
for i in range(lunghezza):
    # Scegliamo un carattere casuale dalla lista
    carattere_scelto = random.choice(caratteri)
    
    # Aggiungiamo il carattere alla password
    password = password + carattere_scelto

# Stampiamo la password generata
print("Password generata:", password)

# Apriamo il file pwd.txt in modalità scrittura
file = open("pwd.txt", "w")

# Scriviamo la password nel file
file.write(password)

# Chiudiamo il file
file.close()

# Messaggio finale
print("Password salvata nel file pwd.txt")

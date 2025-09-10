standardform = -1
desimaler = 1

def velgDesimaler():
    return(int(input("Hvor mange desimaler skal svaret maksimalt inneholde?")))

while True:
    kalkinput = input("\nInput (skriv ´help´ for kommandoer): ")
    try:
        if (kalkinput == "desimaler"):
            desimaler = velgDesimaler()
        elif (kalkinput == "help"):
            print("\n\nSkriv ´desimaler´ for å endre antall desimaler i svaret \nSkriv ´standardform´ for å toggle at svaret blir skrevet på standardform eller ikke \nSkriv inn et regnestykke for å regne det ut")
        elif (kalkinput == "standardform"):
            standardform *= -1
            if (standardform == 1):
                print("\n\nstandardform er nå på")
            else:
                print("\n\nstandardform er nå av")
        else:
            if (standardform == 1):
                result = f"{eval(kalkinput)/(10**(int(len(str(eval(kalkinput))))-1))} * 10^{int(len(str(eval(kalkinput))))-1}"    
            else:
                result = round(eval(kalkinput), desimaler)
            print(f"\n\n{kalkinput} = {result}")
    except:
        print(kalkinput, "er en invalid kommando")












import random

spillere = []
poeng = [0,0]

def info():
    return("Dette er hvordan spille fungerer:")


def ta_navn():
    navn = input("Hva er navnet ditt? ")
    spillere.append(navn)
    return(navn)


def trill_terninger():
    while True:
        trill = input("Vil dere trille terninger? (y/n)")

        if (trill == "y"):
            terning1 = random.randint(1,6)
            print(f"{spillere[0]} trillet {terning1}")
            terning2 = random.randint(1,6)
            print(f"{spillere[1]} trillet {terning2}")

            if (terning1 > terning2):
                poeng[0] += 1
            elif (terning2 > terning1):
                poeng[1] += 1

        elif (trill == "n"):
            break


def start_spill():

    print(info())

    for i in range(2):
        print(f"Navnet ditt er {ta_navn()}")
    
    trill_terninger()
    resultat()

def resultat():
    vinner = poeng.index(max(poeng))
    taper = poeng.index(min(poeng))
    print(f"{spillere[vinner]} vant med {poeng[vinner]} poeng, mot {spillere[taper]} med {poeng[taper]} poeng")


start_spill()
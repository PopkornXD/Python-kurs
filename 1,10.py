import random

variabler = [1.01, -2.65, 5.17, -9.49, 6.48, 12.99]

random_var = variabler[random.randint(0,len(variabler)-1)]

maks = max(variabler)
min = min(variabler)
absolutt = abs(random_var)
avrund = round(random_var, 1)


print ("variablene dine er:")
print (*variabler)

print(f"Det største tallet er: {maks}, det minste er {min}, absoluttverdien til {random_var} er {absolutt}, og den avrundede verdien av {random_var} er {avrund}")
lønn = 0

biler_solgt = int(input("hvor mange biler har du solgt? "))

if (biler_solgt > 70):
    lønn += 5000

lønn += 500*biler_solgt

print("du får ", lønn, "kr i lønn for å ha solgt ", biler_solgt, "biler")
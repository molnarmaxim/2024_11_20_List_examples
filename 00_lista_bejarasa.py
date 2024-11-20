# gyümölcsök kiíratása
gyumolcsok = ['alma', 'körte', 'szilva', 'barack']

print(gyumolcsok)

for gyumolcs in gyumolcsok:
    print(gyumolcs)

# hónapok kiíratása
honapok = ['január', 'február','március', 'április', 'május', 'június', 'július'] 

print(honapok)


print(honapok[0])
print(honapok[1])

# index felhasználása sorszámok megadásához:
    # 1. január
    # 2. február

i = 1
for honap in honapok:
    print(f"{i}. {honap}")
    i = i + 1
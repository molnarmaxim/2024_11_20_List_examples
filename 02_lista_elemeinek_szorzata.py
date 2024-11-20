"""
Hozz létre egy listát számokkal: [2, 4, 6, 8]. 
Írd ki a lista elemeinek szorzatát (azaz a számok szorzatát)!
"""

szamok = [2, 4, 6, 8]
#print(lista[0] * lista[1] * lista[2] * lista[3])

szorzat = 1

for szam in szamok:
    szorzat = szorzat * szam

print(szorzat)
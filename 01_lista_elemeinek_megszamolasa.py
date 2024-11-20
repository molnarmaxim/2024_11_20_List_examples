"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

lista = [5, 8, 12, 15, 22]

hossz = 0
for i in range(5):
    print(lista[i])
    i = i + 1
    hossz = hossz + 1

print(f"Lista elemei len ciklussal: {len(lista)}")
print(f"A lista hossza: {hossz}")
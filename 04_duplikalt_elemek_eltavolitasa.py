"""
Hozz létre egy listát számokkal, ahol előfordulhatnak duplikációk: [1, 2, 2, 3, 3, 4, 5, 5].
Távolítsd el a duplikált számokat, és írd ki az eredményt!
"""

# set-es megoldás
lista = [1, 2, 2, 3, 3, 4, 5, 5]

szett = set(lista)
print(szett)
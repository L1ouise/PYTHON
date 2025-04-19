import random
import math
mot = ["chat", "chien", "Dragon", "oiseau", "Poisson"]
mots_secret = random.choice(mot)

tentatives = len(mots_secret)
print(tentatives)
lettre_trouvee = []

mots_longeur = "_ " * len(mots_secret)

while tentatives > 0 and "_ " in mots_longeur:
    print("la longeur de la lettre est de : ", mots_longeur) 
    print("tentatives restantes : ", tentatives)
    
    lettre = input("entrez une lettre : ").lower()
    if lettre in mots_secret:
        print("bravo tu as trouvé une lettre du mots secret")
        continue
    elif lettre in lettre_trouvee:
        print("vous avez déjà trouvé cette lettre")
        continue
    lettre_trouvee.append(lettre)
    if lettre not in mots_secret:
        print("lettre incorrecte")
        tentatives -= 1
        continue
if "_" not in mots_longeur:
    print("vous avez gagné le mot secret est : ", mots_secret) 
else:
    print("vous avez perdu le mot secret était : ", mots_secret)
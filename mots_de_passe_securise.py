#from fastapi import FastAPI
import string
import random

class PasswordGenerator:
    def __init__(self, lenght: int, level: str):
        self.lenght = lenght
        self.level = level
        self.generate_password = self.generate_password()
    def generate_password(self):
        min_letter = string.ascii_lowercase
        maj_letter = string.ascii_uppercase
        number = string.digits
        special_char = string.punctuation
        
        if self.level == "simple":
            return min_letter
        elif self.level == "moyen":
            return min_letter + maj_letter
        elif self.level == "difficile":
           return min_letter + maj_letter + number + special_char
        else:
            raise ValueError("Niveau de sécurité invalide. Choisissez 'simple', 'moyen' ou 'difficile'.")
    def generer(self):
        return ''.join(random.choice(self.generate_password) for _ in range(self.lenght))   

"""
app = FastAPI()
@app.get("/generer_mot_de_passe")  
def api_generer_mot_de_passe(lenght: int, level: str):
    try:
        generateur = PasswordGenerator(lenght, level)
        return {"mot_de_passe": generateur.generer()}
    except ValueError as e:
        return {"erreur": str(e)}
"""
   
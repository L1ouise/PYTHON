"""
🚀 TaskFlow - Gérez, modifiez et suivez vos tâches intelligemment avec Python & SQLite 📝
Vous avez besoin d’un moyen simple et efficace pour ajouter, modifier, supprimer et consulter vos tâches ? TaskFlow est là pour vous !
✅ Ajoutez vos tâches en toute simplicité
✅ Modifiez une tâche existante au lieu de la supprimer
✅ Supprimez les tâches terminées
✅ Affichez vos tâches sous forme organisée
✅ Sauvegarde automatique avec SQLite pour ne rien perdre
🎯 Pourquoi choisir TaskFlow ?
Parce qu’il offre une gestion complète des tâches avec Python et SQLite sans dépendre d’outils complexes. C’est rapide, léger et facile à utiliser !
💻 Essayez-le maintenant et boostez votre organisation ! 
"""

import sqlite3
class Mestaches:
    def __init__(self, tache=None): #constructeur de la classe avec un paramètre optionnel tache 
        self.conn = sqlite3.connect('taches.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute( """
            CREATE TABLE IF NOT EXISTS taches (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                tache TEXT
            )
        """)
        self.conn.commit()
        
        
        self.ma_list = tache if tache is not None else []
        
        #la fonction d'ajout de tache à la liste
    def ajout_tache(self):
        while True:
            liste = input("Entrer une nouvelle tâche (ou 'exit' pour arreter):")
            self.cursor.execute("INSERT INTO taches (tache) VALUES (?)", (liste,))
            self.conn.commit()
            if liste.lower() == 'exit':
                print("Ajout de tâche arreter.")
                break
            self.ma_list.append(liste)
            print(f"Tâche '{liste}' ajoutée avec succès !")
    
    def supprimer_tache(self):
        print("la liste des tâches ajoutées est :", self.ma_list)
        tache_del = input("Entrer la tâche à supprimer :")
        self.cursor.execute("DELETE FROM taches WHERE tache = ?", (tache_del,))
        self.conn.commit()
        if tache_del in self.ma_list:
            self.ma_list.remove(tache_del)
            print(f"Tâche '{tache_del}' supprimée avec succès !")
        else:
            print(f"Tâche '{tache_del}' non trouvée dans la liste.")
            
    def afficher_tache(self):
        self.cursor.execute("SELECT tache FROM taches")
        tache = self.cursor.fetchall()
        if not self.ma_list:
            print("\n" + "="*20 + "\nListe des tâches :")
        else:
            print("Liste des tâches :")
            for i, tache in enumerate(self.ma_list, start=1):
                print(f"{i}. {tache}")
    
    def modifier_tache(self):
        print("la liste des tâches ajoutées est :", self.ma_list)
        tache_mod = input("Entrer la tâche à modifier :")
        self.cursor.execute("UPDATE taches SET tache = ? WHERE tache = ?", (tache_mod, tache_mod))  
        self.conn.commit()
        if tache_mod in self.ma_list:
            index = self.ma_list.index(tache_mod)
            nouvelle_tache = input("Entrer la nouvelle tâche :")
            self.ma_list[index] = nouvelle_tache
            print(f"Tâche '{tache_mod}' modifiée avec succès en '{nouvelle_tache}' !")
        else:
            print(f"Tâche '{tache_mod}' non trouvée dans la liste.")
        
        print("==========================\n")
        
    def menu(self):
        while True:

            print("Menu :")
            print("1. Ajouter une tâche")
            print("2. Supprimer une tâche")
            print("3. Afficher les tâches")
            print("4. Modifier une tâche")
            print("5. Quitter")
            choix = input("Choisissez une option (1-5) :")
            if choix == '1':
                self.ajout_tache()
            elif choix == '2':
                self.supprimer_tache()
            elif choix == '3':
                self.afficher_tache()
            elif choix == '4':
                self.modifier_tache()
            elif choix == '5':
                print("Au revoir !")
                exit()
            else:
                print("Choix invalide, veuillez réessayer.")


Mes_taches = Mestaches()
Mes_taches.menu()

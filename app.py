
class Eleve:
    def __init__(self, nom, prenom, age, classe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.classe = classe

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans, Classe : {self.classe}"


class Ecole:
    def __init__(self, nom_ecole, specialites, eleves=None):
        self.nom_ecole = nom_ecole
        self.specialites = specialites 
        self.eleves = []

    def inscrire_eleve(self, eleve):
        self.eleves.append(eleve)
        print(f" {eleve.prenom} {eleve.nom} a été inscri avec succès.")

    def afficher_eleves(self):
        if self.eleves is None:
            print(" Aucun élève inscrit pour le moment.")
        else:
            print(f"\n Liste des élèves inscrits à {self.nom_ecole} :")
            for i, eleve in enumerate(self.eleves, 1):
                print(f"{i}. {eleve}")



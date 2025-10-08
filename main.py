class Eleve:
    def __init__(self, nom, prenom, age, classe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.classe = classe

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans, Classe : {self.classe}"


class Ecole(Eleve):
    def __init__(
        self, nom_ecole, specialites, eleves=None, nom="", prenom="", age=0, classe=""
    ):
        super().__init__(nom, prenom, age, classe)
        self.nom_ecole = nom_ecole
        self.specialites = specialites
        self.eleves = []

    def inscrire_eleve(self, eleve):
        self.eleves.append(eleve)
        print(f"{eleve.prenom} {eleve.nom} a été inscrit avec succès chez {self.nom_ecole}.")

    def afficher_eleves(self):
        if self.eleves is None:
            print(" Aucun élève inscrit pour le moment.")
        else:
            print(f"\n Liste des élèves inscrits à {self.nom_ecole} :")
            for i, eleve in enumerate(self.eleves, 1):
                print(f"{i}. {eleve}")

ecole_keyce = Ecole(
    nom_ecole="Keyce Informatique",
    specialites=["Informatique"],
)

print(f"Nom: {ecole_keyce.nom_ecole}")
print(f"Spécialités: {ecole_keyce.specialites} \n\n")

eleve1 = Eleve(nom="GREGOIRE", prenom="Kevin", age=20, classe="Master 1")
eleve2 = Eleve(nom="KODJO", prenom="Winner", age=20, classe="Master 1")
eleve3 = Eleve(nom="PLEBANI", prenom="Lucas", age=20, classe="Master 1")

#print(eleve1)
#print(eleve2)
#print(eleve3)

ecole_keyce.afficher_eleves()

ecole_keyce.inscrire_eleve(eleve1)
ecole_keyce.inscrire_eleve(eleve2)
ecole_keyce.inscrire_eleve(eleve3)

ecole_keyce.afficher_eleves()

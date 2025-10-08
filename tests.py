import pytest
from app import Eleve, Ecole


def test_initialisation_eleve():
    eleve = Eleve(nom="GREGOIRE", prenom="Kevin", age=20, classe="Master 1")

    assert eleve.nom == "GREGOIRE"
    assert eleve.prenom == "Kevin"
    assert eleve.age == 20
    assert eleve.classe == "Master 1"

def test_heritage_eleve():
    ecole = Ecole(
        nom_ecole="Keyce Informatique",
        specialites=["Informatique"],
    )

    assert ecole.nom_ecole == "Keyce Academy"
    assert ecole.specialites == ["Marketing"]
    assert ecole.eleves == []

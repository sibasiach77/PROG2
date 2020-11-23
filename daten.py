import json


def gruppe_speichern(gruppe_name, gruppe_alterskategorie, gruppe_dauer):
    try:
        with open("datenbank_gruppe.json", "r", encoding="utf-8") as datenbank_gruppe:
            gruppen = json.load(datenbank_gruppe)
    except:
        gruppen = {}
    gruppe = {
        "gruppe_name": {
        "Name": gruppe_name,
        "Alterskategorie": gruppe_alterskategorie,
        "Dauer": gruppe_dauer
        }
        }

    gruppen.update(gruppe)

    with open("datenbank_gruppe.json", "w") as datenbank_gruppe:
        json.dump(gruppen, datenbank_gruppe)

    return gruppe_name, gruppe_alterskategorie, gruppe_dauer

def laden():
    try:
        with open("datenbank_gruppe.json", "r", encoding="utf-8") as datenbank_gruppe:
            gruppen = json.load(datenbank_gruppe)
    except:
        gruppen = {}

    return gruppen

def training_speichern(training_datum, training_gruppengroesse):
    try:
        with open("datenbank_training.json", "r", encoding="utf-8") as datenbank_training:
            trainings = json.load(datenbank_training)
    except:
        trainings = {}
    training = {
        "training_datum": {
        "Datum": training_datum,
        "Gruppengrösse": training_gruppengroesse,
        }
        }

    trainings.update(training)

    with open("datenbank_training.json", "w") as datenbank_training:
        json.dump(trainings, datenbank_training)

    return training_datum, training_gruppengroesse

def trainingseinheit_speichern(trainingseinheit_typ, trainingseinheit_ort, trainingseinheit_dauer):
    try:
        with open("datenbank_trainingseinheit.json", "r", encoding="utf-8") as datenbank_trainingseinheit:
            trainingseinheiten = json.load(datenbank_trainingseinheit)
    except:
        trainingseinheiten = {}
    trainingseinheit = {
        "trainingseinheit_name": {
        "Typ": trainingseinheit_typ,
        "Ort": trainingseinheit_ort,
        "Dauer": trainingseinheit_dauer
        }
        }

    trainingseinheiten.update(trainingseinheit)

    with open("datenbank_trainingseinheit.json", "w") as datenbank_trainingseinheit:
        json.dump(trainingseinheiten, datenbank_trainingseinheit)

    return trainingseinheit_typ, trainingseinheit_ort, trainingseinheit_dauer


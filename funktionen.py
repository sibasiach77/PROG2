import json

def trainingseinheiten_oeffnen():
    try:
        with open("datenbank_trainingseinheiten.json", "r", encoding="utf-8") as datenbank_trainingseinheiten:
            trainingseinheiten = json.load(datenbank_trainingseinheiten)
    except:
        trainingseinheiten = {}

    return trainingseinheiten


def erfassen_speichern(name_trainingseinheit_erfassen_antwort,
                       typ_erfassen_antwort,
                       ort_erfassen_antwort,
                       dauer_min_erfassen_antwort,
                       dauer_max_erfassen_antwort,
                       gruppengroesse_min_erfassen_antwort,
                       gruppengroesse_max_erfassen_antwort):

    trainingseinheiten = trainingseinheiten_oeffnen()

    trainingseinheit = {
        name_trainingseinheit_erfassen_antwort: {
            "name": name_trainingseinheit_erfassen_antwort,
            "typ": typ_erfassen_antwort,
            "ort": ort_erfassen_antwort,
            "gruppengroesse_min": gruppengroesse_min_erfassen_antwort,
            "gruppengroesse_max": gruppengroesse_max_erfassen_antwort,
            "dauer_min": dauer_min_erfassen_antwort,
            "dauer_max": dauer_max_erfassen_antwort,
        }
    }
    trainingseinheiten.update(trainingseinheit)

    with open("datenbank_trainingseinheiten.json", "w") as datenbank_trainingseinheiten:
        json.dump(trainingseinheiten, datenbank_trainingseinheiten)

    return name_trainingseinheit_erfassen_antwort, \
           typ_erfassen_antwort, \
           ort_erfassen_antwort, \
           dauer_min_erfassen_antwort, \
           dauer_max_erfassen_antwort, \
           gruppengroesse_min_erfassen_antwort, \
           gruppengroesse_max_erfassen_antwort


def filter(datum_abfrage_antwort,
           typ_abfrage_antwort,
           ort_abfrage_antwort,
           gruppengroesse_abfrage_antwort,
           dauer_abfrage_antwort):

    trainingseinheiten = trainingseinheiten_oeffnen()
    """
    Der Dict Trainingseinheiten wird in die Sequenzen key (name) und 
    values (typ, ort, gruppengroesse_min/max, dauer_min/max geteilt.
    """
    liste_vorschlaege = []
    for key, value in trainingseinheiten.items():
        # Es wird bei allen keys überprüft ob sie der entsprechenden Variabel entsprechen.
        if trainingseinheiten[key]["typ"] == typ_abfrage_antwort \
        and trainingseinheiten[key]["ort"] == ort_abfrage_antwort \
        and trainingseinheiten[key]["gruppengroesse_min"] <= gruppengroesse_abfrage_antwort \
        and trainingseinheiten[key]["gruppengroesse_max"] >= gruppengroesse_abfrage_antwort \
        and trainingseinheiten[key]["dauer_min"] <= dauer_abfrage_antwort \
        and trainingseinheiten[key]["dauer_max"] >= dauer_abfrage_antwort:
            # Die Values deren Keys den Variabeln entsprechen, werden der liste_vorschlaege hinzugefügt.
            liste_vorschlaege.append([trainingseinheiten[key]["name"],
                                 trainingseinheiten[key]["typ"],
                                 trainingseinheiten[key]["ort"],
                                 trainingseinheiten[key]["gruppengroesse_min"],
                                 trainingseinheiten[key]["gruppengroesse_max"],
                                 trainingseinheiten[key]["dauer_min"],
                                 trainingseinheiten[key]["dauer_max"]])
        # Entsprechen die Variabeln keinen Keys der Datenbank, wird der String "kein Vorschlag" in die liste_vorschlaege gespeichert.
        else:
            liste_vorschlaege = ["kein Vorschlag"]

    return liste_vorschlaege, datum_abfrage_antwort




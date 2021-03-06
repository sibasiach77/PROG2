import json


# Funktion zum Öffnen der datenbank_trainingseinheiten.
def trainingseinheiten_oeffnen():
    try:
        with open('datenbank_trainingseinheiten.json', 'r', encoding='utf-8') as datenbank_trainingseinheiten:
            # Inhalt der Datenbank wird als Dictonary trainingseinheiten gespeichert.
            trainingseinheiten = json.load(datenbank_trainingseinheiten)
    except:
        trainingseinheiten = {}

    return trainingseinheiten


# Funktion zum Öffnen der datenbank_trainings_gespeichert.
def trainings_gespeichert_oeffnen():
    try:
        with open('datenbank_trainings_gespeichert.json', 'r', encoding='utf-8') as datenbank_trainings_gespeichert:
            # Inhalt der Datenbank wird als Dictonary trainings_gespeichert gespeichert.
            trainings_gespeichert = json.load(datenbank_trainings_gespeichert)
    except:
        trainings_gespeichert = {}

    return trainings_gespeichert


def erfassen_speichern(name_trainingseinheit_erfassen_antwort,
                       typ_erfassen_antwort,
                       ort_erfassen_antwort,
                       dauer_min_erfassen_antwort,
                       dauer_max_erfassen_antwort,
                       gruppengroesse_min_erfassen_antwort,
                       gruppengroesse_max_erfassen_antwort):
    # Funktion trainingseinheiten_oeffnen wird ausgeführt, gespeicherte Trainingseinheiten werden geöffnet.
    trainingseinheiten = trainingseinheiten_oeffnen()

    # Neuer Dictonary trainingseinheit wird mit den eingegebenen Daten befüllt.
    trainingseinheit = {
        name_trainingseinheit_erfassen_antwort: {
            'name': name_trainingseinheit_erfassen_antwort,
            'typ': typ_erfassen_antwort,
            'ort': ort_erfassen_antwort,
            'gruppengroesse_min': gruppengroesse_min_erfassen_antwort,
            'gruppengroesse_max': gruppengroesse_max_erfassen_antwort,
            'dauer_min': dauer_min_erfassen_antwort,
            'dauer_max': dauer_max_erfassen_antwort,
        }
    }
    # Gespeicherte Trainingseinheiten werden mit neuer Trainingseinheit ergänzt.
    trainingseinheiten.update(trainingseinheit)

    # Der Neue Dictonary wird in der Json-Datei gespeichert.
    with open('datenbank_trainingseinheiten.json', 'w') as datenbank_trainingseinheiten:
        json.dump(trainingseinheiten, datenbank_trainingseinheiten)

    return name_trainingseinheit_erfassen_antwort, \
           typ_erfassen_antwort, \
           ort_erfassen_antwort, \
           dauer_min_erfassen_antwort, \
           dauer_max_erfassen_antwort, \
           gruppengroesse_min_erfassen_antwort, \
           gruppengroesse_max_erfassen_antwort


# Filterfunktion zum Abgleich der gespeicherten Trainingseinheiten und der Abfrage.
def filter(typ_abfrage_antwort,
           ort_abfrage_antwort,
           gruppengroesse_abfrage_antwort,
           dauer_abfrage_antwort,
           datum_abfrage_antwort):
    # Funktion trainingseinheiten_oeffnen wird ausgeführt, gespeicherte Trainingseinheiten werden geöffnet.
    trainingseinheiten = trainingseinheiten_oeffnen()

    # Ein leerer Dict vorschlaege wird geöffnet.
    vorschlaege = {}

    """
    Der Dict Trainingseinheiten wird in die Sequenzen key (name) und 
    values (typ, ort, gruppengroesse_min/max, dauer_min/max geteilt.
    """
    for key, value in trainingseinheiten.items():
        # Es wird bei allen keys überprüft ob sie der entsprechenden Variabel entsprechen.
        if trainingseinheiten[key]['typ'] == typ_abfrage_antwort \
                and trainingseinheiten[key]['ort'] == ort_abfrage_antwort \
                and trainingseinheiten[key]['gruppengroesse_min'] <= gruppengroesse_abfrage_antwort \
                and trainingseinheiten[key]['gruppengroesse_max'] >= gruppengroesse_abfrage_antwort \
                and trainingseinheiten[key]['dauer_min'] <= dauer_abfrage_antwort \
                and trainingseinheiten[key]['dauer_max'] >= dauer_abfrage_antwort:
            # Die Values deren Keys den Variabeln entsprechen, werden dem Dict vorschlaege hinzugefügt.
            vorschlag = {
                trainingseinheiten[key]['name']: {
                    'name': trainingseinheiten[key]['name'],
                    'typ': trainingseinheiten[key]['typ'],
                    'ort': trainingseinheiten[key]['ort'],
                    'gruppengroesse': gruppengroesse_abfrage_antwort,
                    'dauer': dauer_abfrage_antwort,
                    'datum': datum_abfrage_antwort
                }
            }
            vorschlaege.update(vorschlag)
    """
    Der Dict vorschlaege wird in der Datenbank Vorschläge gespeichert.
    Da die Vorschläge immer erneuert werden, werden sie immer überschrieben.
    """

    """
    Entsprechen die Variabeln keinen Keys der Datenbank (= der Dict vorschlaege ist leer), 
    wird der String "keine Vorschläge" in vorschlaege gespeichert.
    Die Ausgabe "keine Vorschläge" könnte ebenfalls gespeichert werden. Es wird jedoch davon ausgegangen, dass der User
    dies nicht macht und eine neue Abfrage startet.
    """
    if not vorschlaege:
        vorschlaege = {'name': {
            'name': 'keine Vorschläge'
        }
        }
    # Die datenbank_vorschlaege wird neu gespeichert.
    with open('datenbank_vorschlaege.json', 'w') as datenbank_vorschlaege:
        json.dump(vorschlaege, datenbank_vorschlaege)

    # Vorschlaege werden an main.py zurückgegeben.
    return vorschlaege


def vorschlag_speichern_funktion(name_speichern):
    # Die Datenbank datenkbank_vorschlaege wird geöffnet.
    try:
        with open('datenbank_vorschlaege.json', 'r', encoding='utf-8') as datenbank_vorschlaege:
            # Die Inhalte (Dict) der datenbank_vorschlaege werden in der Variabel vorschlaege gespeichert.
            vorschlaege = json.load(datenbank_vorschlaege)
    except:
        vorschlaege = {}

    """ Die Values aus dem Dict vorschlaege werden anhand der Variabel bzw. dem Key name_speichern aufgerufen 
    und in neuen Variabeln gespeichert.
    """
    typ_speichern = vorschlaege[name_speichern]['typ']
    ort_speichern = vorschlaege[name_speichern]['ort']
    gruppengroesse_speichern = vorschlaege[name_speichern]['gruppengroesse']
    dauer_speichern = vorschlaege[name_speichern]['dauer']
    datum_speichern = vorschlaege[name_speichern]['datum']

    # Die Datenbank trainings_gespeichert wird geöffnet.
    trainings_gespeichert = trainings_gespeichert_oeffnen()

    # Ein Neues Dict namens training_speichern wird eröffnet und mit den Variabeln befüllt.
    training_speichern = {
        datum_speichern: {
            'trainings': {
                name_speichern: {
                    'name': name_speichern,
                    'typ': typ_speichern,
                    'ort': ort_speichern,
                    'dauer': dauer_speichern,
                }
            },
            'gruppengroesse': gruppengroesse_speichern
        }
    }

    """
    Gruppengrösse ist ausserhalb der anderen Keys, da diese in einem Training immer gleich gross ist.
    Es wird immer nur die Gruppengrösse der ersten erfassten Trainingseinheit ausgegeben. Es wird davon
    ausgegangen, dass der User diese für alle Trainingseinheiten richtig erfasst.
    """

    """
    Es wird überprüft, ob das Trainingsdatum bereits im Dict vorhanden ist.
    Falls das Trainingsdatum bereits vorhanden und der Name noch nicht, wird diese Trainingseinheit als neuer Dict
    hinzugefügt. Ansonsten wird der Dict überschrieben.
    """

    if datum_speichern in trainings_gespeichert.keys():
        trainings_gespeichert[datum_speichern]['trainings'][name_speichern] = \
            training_speichern[datum_speichern]['trainings'][name_speichern]
    else:
        trainings_gespeichert[datum_speichern] = training_speichern[datum_speichern]

    # Der Dict training_speichern wird der Variabel trainings_gespeichert hinzugefügt.
    with open('datenbank_trainings_gespeichert.json', 'w') as datenbank_trainings_gespeichert:
        json.dump(trainings_gespeichert, datenbank_trainings_gespeichert)

    # Die Datenbank trainings_gespeichert wird erneut geöffnet.
    trainings_gespeichert = trainings_gespeichert_oeffnen()

    # Der dict trainings_gespeichert wird returned.
    return trainings_gespeichert


def gesamtdauer(training_datum, new_training):
    # Die Datenbank trainings_gespeichert wird geöffnet.
    trainings_gespeichert = trainings_gespeichert_oeffnen()
    # Ist die Variabel dauer_gesamt vorhanden, wird sie neu aus dem Dictonary aufgerufen und gespeichert.
    if 'dauer_gesamt' in trainings_gespeichert[training_datum]:
        dauer_gesamt = trainings_gespeichert[training_datum]['dauer_gesamt']
    else:
        # Ist die Variabel dauer_gesamt noch nicht vorhanden, wird sie neu mit dem Wert "0" erfasst.
        dauer_gesamt = 0
    # Die Variabel dauer_gesamt wird mit der Dauer der neu erfassten Trainingseinheit new_training addiert.
    dauer_gesamt = dauer_gesamt + trainings_gespeichert[training_datum]['trainings'][new_training]['dauer']

    # Die neue dauer_gesamt des Dictonary wird in der Variabel dauer_gesamt gespeichert.
    trainings_gespeichert[training_datum]['dauer_gesamt'] = dauer_gesamt

    # Der neue Dictonary wird in der datenbank_trainings_gepseichert gespeichert.
    with open('datenbank_trainings_gespeichert.json', 'w') as datenbank_trainings_gespeichert:
        json.dump(trainings_gespeichert, datenbank_trainings_gespeichert)

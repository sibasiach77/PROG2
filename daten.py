import json


def gruppe_speichern(gruppe_name, gruppe_alterskategorie, gruppe_dauer):
    try:
        with open("datenbank.json", "r", encoding="utf-8") as datenbank:
            gruppen = json.load(datenbank)
    except:
        gruppen = {}
    gruppe = {
        "Name": gruppe_name: {
            "Alterskateogire": gruppe_alterskategorie,
            "Dauer": gruppe_dauer
        }
    }
    gruppen.update(gruppe)
    with open("datenbank.json", "w") as datenbank:
        json.dump(gruppen, datenbank)
    return "Daten gespeichert"

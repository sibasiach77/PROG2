


def laden():
    try:
        with open("datenbank_abfrage.json", "r", encoding="utf-8") as datenbank_abfrage:
            abfragen = json.load(datenbank_abfrage)
    except:
        print("Es wurden noch keine Trainings erfasst.")
        abfragen = {}

    return abfragen


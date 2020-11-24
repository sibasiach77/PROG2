from flask import Flask
# Mithilfe von render_template werden Daten an HTML gesendet.
from flask import render_template
# Mithilfe von request werden Daten abgefangen.
from flask import request
import json
from datetime import datetime

app = Flask("trainingsplaner")

# Rendern des index.html Templates, für das Anzeigen der index.html Page
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/abfrage", methods=['POST', 'GET'])
def abfrage():
    if request.method == 'POST':
        datum_abfrage_antwort = request.form['datum_abfrage']
        typ_abfrage_antwort = request.form['typ_abfrage']
        ort_abfrage_antwort = request.form['ort_abfrage']
        gruppengroesse_abfrage_antwort = request.form['gruppengroesse_abfrage']
        dauer_min_abfrage_antwort = request.form['dauer_min_abfrage']
        dauer_max_abfrage_antwort = request.form['dauer_max_abfrage']
        # in Json speichern
        try:
            with open("datenbank_abfrage.json", "r", encoding="utf-8") as datenbank_abfrage:
                abfragen = json.load(datenbank_abfrage)
        except:
            abfragen = {}

        abfrage = {
            "Abfrage": {
                "Datum": datum_abfrage_antwort,
                "Typ": typ_abfrage_antwort,
                "Ort": ort_abfrage_antwort,
                "Gruppengroesse": gruppengroesse_abfrage_antwort,
                "Dauer_min": dauer_min_abfrage_antwort,
                "Dauer_max": dauer_max_abfrage_antwort
            }
        }
        abfragen.update(abfrage)

        with open("datenbank_abfrage.json", "w") as datenbank_abfrage:
            json.dump(abfragen, datenbank_abfrage)

        return abfrage
    return render_template('abfrage.html')

@app.route("/erfassen", methods=['POST', 'GET'])
def erfassen():
    if request.method == 'POST':
        name_trainingseinheit_erfassen_antwort = request.form['name_trainingseinheit']
        typ_erfassen_antwort = request.form['typ_erfassen']
        ort_erfassen_antwort = request.form['ort_erfassen']
        dauer_min_erfassen_antwort = request.form['dauer_min_erfassen']
        dauer_max_erfassen_antwort = request.form['dauer_max_erfassen']
        gruppengroesse_min_erfassen_antwort = request.form['gruppengroesse_min_erfassen']
        gruppengroesse_max_erfassen_antwort = request.form['gruppengroesse_max_erfassen']

        try:
            with open("datenbank_training.json", "r", encoding="utf-8") as datenbank_trainingseinheiten:
                trainingseinheiten = json.load(datenbank_trainingseinheiten)
        except:
            trainingseinheiten = {}

        x = datetime.now()

        trainingseinheit = {
            "Trainingseinheit " + str(x): {
                "Name": name_trainingseinheit_erfassen_antwort,
                "Typ": typ_erfassen_antwort,
                "Ort": ort_erfassen_antwort,
                "Dauer_min": dauer_min_erfassen_antwort,
                "Dauer_max": dauer_max_erfassen_antwort,
                "Gruppengroesse_min": gruppengroesse_min_erfassen_antwort,
                "Gruppengroesse_max": gruppengroesse_max_erfassen_antwort
            }
        }
        trainingseinheiten.update(trainingseinheit)

        with open("datenbank_trainingseinheiten.json", "w") as datenbank_trainingseinheiten:
            json.dump(trainingseinheiten, datenbank_trainingseinheiten)

        return trainingseinheiten
    return render_template('erfassen.html')

"""

Hier ist noch eine Baustelle.
Auf Übersicht sollen die angenommenen Trainingsvorschläge gespeichert werden.
"""

@app.route("/uebersicht")
def uebersicht():
    try:
        with open("datenbank_abfrage.json", "r", encoding="utf-8") as datenbank_abfrage:
            abfragen = json.load(datenbank_abfrage)
    except:
        print("Es wurden noch keine Trainings erfasst.")
        abfragen = {}
    for schluessel, werte in abfragen.items():
        print(werte)
    return render_template(
        "uebersicht.html",
        daten_uebersicht=werte
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
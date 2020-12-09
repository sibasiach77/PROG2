from flask import Flask
# Mithilfe von render_template werden Daten an HTML gesendet.
from flask import render_template
# Mithilfe von request werden Daten abgefangen.
from flask import request
from trainingsplaner_1.PROG2.funktionen import *
import json

app = Flask(__name__)

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
        gruppengroesse_abfrage_antwort = int(gruppengroesse_abfrage_antwort)
        dauer_abfrage_antwort = request.form['dauer_abfrage']
        dauer_abfrage_antwort = int(dauer_abfrage_antwort)

        vorschlaege = filter(typ_abfrage_antwort,
                             ort_abfrage_antwort,
                             gruppengroesse_abfrage_antwort,
                             dauer_abfrage_antwort,
                             datum_abfrage_antwort)

        return render_template('vorschlaege.html', vorschlaege=vorschlaege, datum_training=datum_abfrage_antwort)
    return render_template('abfrage.html')

@app.route("/erfassen", methods=['POST', 'GET'])
def erfassen():
    if request.method == 'POST':
        # Die Antworten aus dem Formular erfassen.html werden in Variablen gespeichert.
        name_trainingseinheit_erfassen_antwort = request.form['name_trainingseinheit']
        name_trainingseinheit_erfassen_antwort = name_trainingseinheit_erfassen_antwort.capitalize()
        typ_erfassen_antwort = request.form['typ_erfassen']
        ort_erfassen_antwort = request.form['ort_erfassen']
        dauer_min_erfassen_antwort = request.form['dauer_min_erfassen']
        dauer_min_erfassen_antwort = int(dauer_min_erfassen_antwort)
        dauer_max_erfassen_antwort = request.form['dauer_max_erfassen']
        dauer_max_erfassen_antwort = int(dauer_max_erfassen_antwort)
        gruppengroesse_min_erfassen_antwort = request.form['gruppengroesse_min_erfassen']
        gruppengroesse_min_erfassen_antwort = int(gruppengroesse_min_erfassen_antwort)
        gruppengroesse_max_erfassen_antwort = request.form['gruppengroesse_max_erfassen']
        gruppengroesse_max_erfassen_antwort = int(gruppengroesse_max_erfassen_antwort)

        # Die Funktion erfassen_speichern aus funktionen.py wird mit den Variablen durchgeführt.
        erfassen_speichern(name_trainingseinheit_erfassen_antwort,
                           typ_erfassen_antwort, ort_erfassen_antwort,
                           dauer_min_erfassen_antwort,
                           dauer_max_erfassen_antwort,
                           gruppengroesse_min_erfassen_antwort,
                           gruppengroesse_max_erfassen_antwort)

        return render_template('erfassen.html')
    return render_template('erfassen.html')

"""
Hier ist noch eine Baustelle.
Auf Übersicht sollen die angenommenen Trainingsvorschläge gespeichert werden.
"""
@app.route("/uebersicht")
def uebersicht():
    return render_template('uebersicht.html')

@app.route("/vorschlag_speichern", methods=['POST', 'GET'])
def vorschlag_speichern():
    if request.method == 'POST':
        # Die erhaltene Info des Users aus der vorschlag.html wird in der Variabel name gespeichert.
        name = request.form['name']
        # Die Datenbank datenkbank_vorschlaege wird geöffnet.
        try:
            with open("datenbank_vorschlaege.json", "r", encoding="utf-8") as datenbank_vorschlaege:
                # Die Inhalte (Dict) der datenbank_vorschlaege werden in der Variabel vorschlaege gespeichert.
                vorschlaege = json.load(datenbank_vorschlaege)
        except:
            vorschlaege = {}
        # Die Werte aus dem Dict vorschlaege werden aufgerufen und in den Variabeln gespeichert.
        typ_speichern = vorschlaege[name]["typ"]
        ort_speichern = vorschlaege[name]["ort"]
        gruppengroesse_speichern = vorschlaege[name]["gruppengroesse"]
        dauer_speichern = vorschlaege[name]["dauer"]
        datum_speichern = vorschlaege[name]["datum"]

        # Die Datenbank trainings_gespeichert wird geöffnet.
        try:
            with open("datenbank_trainings_gespeichert.json", "r", encoding="utf-8") as datenbank_trainings_gespeichert:
                # Die Inhalte der Datenbank trainings_gespeichert wird in die Variabel trainings_gespeichert gespeichert.
                trainings_gespeichert = json.load(datenbank_trainings_gespeichert)
        except:
            trainings_gespeichert = {}

        """
        Hier sollte überprüft werden, ob das zu speichernde Datum bereits als Training angelegt ist.
        Wenn ja, soll die Trainingseinheit dem Datum hinzugefügt werden. 
        for datum_trainings in trainings_gespeichert.keys():
            if datum_speichern == datum_trainings:
        """

        # Ein Neues Dict namens training_speichern wird eröffnet und mit den Variabeln befüllt.
        training_speichern = {
            datum_speichern: {
                name: {
                    "name": name,
                    "typ": typ_speichern,
                    "ort": ort_speichern,
                    "gruppengroesse": gruppengroesse_speichern,
                    "dauer": dauer_speichern,
                }
            }
        }

        # Der Dict training_speichern wird der Variabel trainings_gespeichert hinzugefügt.
        trainings_gespeichert.update(training_speichern)

        # Der Dict training_speichern wird der Varabel trainings_gespeichert hinzugefügt.
        with open("datenbank_trainings_gespeichert.json", "w") as datenbank_trainings_gespeichert:
            json.dump(trainings_gespeichert, datenbank_trainings_gespeichert)

        # Die Datenbank trainings_gespeichert wird erneut geöffnet.
        try:
            with open("datenbank_trainings_gespeichert.json", "r", encoding="utf-8") as datenbank_trainings_gespeichert:
                # Die Inhalte der Datenbank werden als Variabel trainings_gespeichert gespeichert.
                trainings_gespeichert = json.load(datenbank_trainings_gespeichert)
        except:
            trainings_gespeichert = {}

    # uebersicht.html wird gerendert und die Variabel trainings_gespeichert wird mitgegeben.
    return render_template('uebersicht.html', trainings_gespeichert = trainings_gespeichert)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
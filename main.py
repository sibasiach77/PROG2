from flask import Flask
# Mithilfe von render_template werden Daten an HTML gesendet.
from flask import render_template
# Mithilfe von request werden Daten abgefangen.
from flask import request
from trainingsplaner.funktionen import *

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
        gruppengroesse_abfrage_antwort = float(gruppengroesse_abfrage_antwort)
        dauer_abfrage_antwort = request.form['dauer_abfrage']
        dauer_abfrage_antwort = float(dauer_abfrage_antwort)

        liste_vorschlaege = filter(typ_abfrage_antwort,
                                   ort_abfrage_antwort,
                                   gruppengroesse_abfrage_antwort,
                                   dauer_abfrage_antwort)

        return render_template('vorschlaege.html', liste_vorschlaege=liste_vorschlaege, datum_training=datum_abfrage_antwort)
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
        dauer_min_erfassen_antwort = float(dauer_min_erfassen_antwort)
        dauer_max_erfassen_antwort = request.form['dauer_max_erfassen']
        dauer_max_erfassen_antwort = float(dauer_max_erfassen_antwort)
        gruppengroesse_min_erfassen_antwort = request.form['gruppengroesse_min_erfassen']
        gruppengroesse_min_erfassen_antwort = float(gruppengroesse_min_erfassen_antwort)
        gruppengroesse_max_erfassen_antwort = request.form['gruppengroesse_max_erfassen']
        gruppengroesse_max_erfassen_antwort = float(gruppengroesse_max_erfassen_antwort)

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

@app.route("/vorschlag_speichern")
def vorschlag_speichern():
    try:
        with open("datenbank_vorschlaege_gespeichert.json", "r", encoding="utf-8") as datenbank_vorschlaeg_gespeichert:
            vorschlaege_gespeichert = json.load(datenbank_vorschlaege_gespeichert)
    except:
        vorschlaege_gespeichert = {}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
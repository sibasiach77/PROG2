from flask import Flask
# Mithilfe von render_template werden Daten an HTML gesendet.
from flask import render_template
# Mithilfe von request werden Daten abgefangen.
from flask import request

# Aus der Python Datei Daten wird die Funktion gruppe_speichern importiert.

from daten import gruppe_seichern

app = Flask("trainingsplaner")

# #Rendern des index.html Templates, für das Anzeigen der index.html Page
@app.route('/trainingsplaner')
def home():
    return render_template("index.html")

# Auf dieser Seite ist ein Formular.
# Deshalb wurden die Methoden get und post gesetzt.

@app.route("/gruppe", methods=['POST', 'GET'])
def eingabe_gruppe():
    if request.method == 'POST':
        gruppe_name = request.form['gruppe_name_erfassen']
        gruppe_alterskategorie = request.form['gruppe_alterskategorie_erfassen']
        gruppe_dauer = request.form['gruppe_dauer_erfassen']
        # in Json speichern
        antwort_gruppe = gruppe_speichern(gruppe_name, gruppe_alterskategorie, gruppe_dauer)
        return 'Daten empfangen: ' + (antwort_gruppe)
    return render_template('gruppe.html')

@app.route("/training", methods=['POST', 'GET'])
def eingabe_training():
    if request.method == 'POST':
        training_datum = request.form['training_datum_erfassen']
        training_grueppengroesse = request.form['training_gruppengroesse_erfassen']
        # in Json speichern
        antwort_training = training_speichern(training_datum, training_grueppengroesse)
        return 'Daten empfangen: ' + (antwort_training)
    return render_template('training.html')

@app.route("/trainingseinheit", methods=['POST', 'GET'])
def eingabe_trainingseinheit():
    if request.method == 'POST':
        trainingseinheit_typ = request.form['trainingseinheit_typ_erfassen']
        trainingseinheit_ort = request.form['trainingseinheit_ort_erfassen']
        trainingseinheit_dauer = request.form['trainingseinheit_dauer_erfassen']
        # in Json speichern
        antwort_trainingseinheit = trainingseinheit_speichern(trainingseinheit_typ, trainingseinheit_ort, trainingseinheit_dauer)
        return 'Daten empfangen: ' + (antwort_trainingseinheit)
    return render_template('trainingseinheit.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask
# Mithilfe von render_template werden Daten an HTML gesendet.
from flask import render_template
# Mithilfe von request werden Daten abgefangen.
from flask import request

#
from daten import speichern

app = Flask("trainingsplaner")

# Startseite der URL
@app.route('/trainingsplaner')
def begruessung():
    return render_template('index.html', name="Nadine")

# Auf dieser Seite ist ein Formular.
# Deshalb wurden die Methoden get und post gesetzt.

@app.route("/gruppe", methods=['POST', 'GET'])
def eingabe_gruppe():
    if request.method == 'POST':
        gruppe = request.form['gruppe_erfassen']
        # in Json speichern
        antwort = speichern(gruppe)
        return 'Daten empfangen: ' + (antwort)
    return render_template('gruppe.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
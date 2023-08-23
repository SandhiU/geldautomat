from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

# Test-Benutzer-Daten (Simulation der Datenbank)
benutzerdaten = [
    {"benutzername": "benutzer1", "pin": "1234", "benutzer_id": 1},
    {"benutzername": "benutzer2", "pin": "5678", "benutzer_id": 2}
]

# die HTML-File beim Start der App zu öffnen
@app.route('/')
def anmeldeschnittstelle():
    return render_template('anmelden.html')

@app.route('/hauptschnittstelle')
def hauptschnittstelle():
    benutzername = request.args.get('benutzername')
    return render_template('hauptschnittstelle.html', benutzername=benutzername)

# die App mit dem HTML-Form zu verbinden
@app.route('/backend_almeldeendpunkt', methods=['POST'])
def almelden():
    benutzername = request.form.get('benutzername')
    pin = request.form.get('pin')

    benutzer = next((benutzer for benutzer in benutzerdaten if benutzer["benutzername"] == benutzername and benutzer["pin"] == pin), None) # nach einer Übereinstimmung in der Datenbank zu suchen

    if benutzer:
        return redirect('/hauptschnittstelle?benutzername=' + benutzername) # bei Erfolg leitet es auf die Hauptschnittstelle um.
    else:
        return jsonify({"erfolg": False, "nachricht": "Ihre Anmeldedaten sind ungueltig."}) # bei Erfolg gibt es falsch true zurück

@app.route('/abmelden')
def abmelden():
    return redirect('/')

@app.route('/aufladen')
def aufladen():
    benutzername = request.args.get('benutzername')
    return render_template('aufladen.html', benutzername=benutzername)

@app.route('/backend_aufladen', methods=['POST'])
def backend_aufladen():
    benutzername = request.form.get('benutzername')
    schein = request.form.get('schein')
    return redirect('/hauptschnittstelle?benutzername=' + benutzername)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True) # die App auszuführen
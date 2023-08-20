from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Test-Benutzer-Daten
benutzerdaten = [
    {"benutzername": "benutzer1", "pin": "1234", "benutzer_id": 1},
    {"benutzername": "benutzer2", "pin": "5678", "benutzer_id": 2}
]

@app.route('/')
def index():
    return send_file('anmelden.html')

@app.route('/backend_almeldeendpunkt', methods=['POST'])
def almelden():
    benutzername = request.form.get('benutzername')
    pin = request.form.get('pin')

    benutzer = next((benutzer for benutzer in benutzerdaten if benutzer["benutzername"] == benutzername and benutzer["pin"] == pin), None)

    if benutzer:
        return jsonify({"success": True, "benutzer_id": benutzer["benutzer_id"]})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

if __name__ == '__main__':
    app.run(debug=True)
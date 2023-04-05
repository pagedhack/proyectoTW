#importe de base de datos
from Control import control

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/invernadero')
def invernadero():
    return jsonify({"Control Invernadero" + "- semana 1" : control})

@app.route('/invernadero/<int:control_fecha>')
def getDatos(control_fecha):
    datos = [dato for dato in control if dato['fecha'] == control_fecha]
    return jsonify(datos[0])

if __name__=='__main__':
    app.run(debug=True)
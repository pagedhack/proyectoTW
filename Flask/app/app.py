#importe de base de datos
from Control import control

from flask import Flask, jsonify

# Cambios Jorge
from config import config
from flask_mysqldb import MySQL


app = Flask(__name__)

conexion = MySQL(app)

@app.route('/invernadero')
#def invernadero():
 #   return jsonify({"Control Invernadero" + "- semana 1" : control})
def listar_dias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT temperatura FROM control"
        cursor.execute(sql)
        datos = cursor.fetchall()
        controles = []
        for fila in datos:
            cnt={'temperatura':fila[0]}
            controles.append(cnt)
        return jsonify({'controles':controles, 'mensaje':"Controles listados."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

def pagina_no_econtrada(error):
    return "<h1>La página que intentas buscar no existe ...</h1>"

@app.route('/invernadero/<int:control_fecha>')
def getDatos(control_fecha):
    datos = [dato for dato in control if dato['fecha'] == control_fecha]
    return jsonify(datos[0])

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_econtrada)
    app.run()
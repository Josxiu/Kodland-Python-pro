# Generador de contraseñas seguras con Flask
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Elementos que se pueden usar en la contraseña
ELEMENTOS = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def generar_contrasena(longitud):
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(ELEMENTOS)
    return contrasena


# Una sola ruta: GET muestra el formulario, POST genera la contraseña
@app.route("/", methods=["GET", "POST"])
def inicio():
    contrasena = None
    if request.method == "POST":
        longitud = int(request.form["longitud"])
        longitud = max(4, min(longitud, 50))  # longitud entre 4 y 50
        contrasena = generar_contrasena(longitud)
    return render_template("index.html", contrasena=contrasena)


if __name__ == "__main__":
    app.run(debug=True)

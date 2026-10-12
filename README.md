# Generador de contraseñas

Página web hecha con **Flask** que genera contraseñas seguras y aleatorias.

## ¿Qué hace?
- Muestra un formulario donde el usuario escribe la longitud de la contraseña (de 4 a 50 caracteres).
- Al pulsar **Generar**, crea una contraseña al azar con letras mayúsculas, minúsculas, números y símbolos.
- Muestra la contraseña generada en la misma página.

## Funciones de Flask que usa
- `Flask(__name__)`: crea la aplicación.
- `@app.route("/", methods=["GET", "POST"])`: define la página de inicio y acepta el envío del formulario.
- `request.form`: lee la longitud que escribió el usuario.
- `render_template`: muestra la plantilla HTML y le pasa la contraseña (plantilla Jinja con `{% if %}` y `{{ }}`).

## Cómo ejecutarlo
1. Instalar las librerías:
   ```
   pip install -r requirements.txt
   ```
2. Ejecutar:
   ```
   python app.py
   ```
3. Abrir en el navegador: http://127.0.0.1:5000

## Estructura
```
generador-contrasenas/
├── app.py              # código de Flask
├── templates/
│   └── index.html      # página con el formulario
├── requirements.txt    # librerías necesarias
└── README.md           # este archivo
```

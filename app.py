from flask import Flask
from configs.configuracion import get_config
from controllers.auth import registrar_usuario, iniciar_sesion, cerrar_sesion, pag_home, verificar_otp

app = Flask(__name__)
# Configuracion de la app
config = get_config()
# Clave secreta para sesiones
app.secret_key = config['key']

# Ruta de inicio


@app.route('/')
def home():
    return pag_home()

# Ruta de registro


@app.route('/register', methods=['GET', 'POST'])
def register():
    return registrar_usuario()

# Ruta de inicio de sesion


@app.route('/login', methods=['GET', 'POST'])
def login():
    return iniciar_sesion()

# Ruta de cerrar sesion


@app.route('/logout')
def logout():
    return cerrar_sesion()


@app.route('/otp', methods=['GET', 'POST'])
def otp():
    return verificar_otp()


if __name__ == "__main__":
    app.run(debug=True)

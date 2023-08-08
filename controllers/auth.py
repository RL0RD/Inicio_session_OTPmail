
from flask import request, session, redirect, url_for, render_template, flash
import re
from configs.db import verificar_usuario, crear_usuario, verificar_correo
from configs.correos import enviar_correo_otp
from configs.cifrado import encrypt_text, decrypt_text, read_key_from_file


def registrar_usuario():
    if 'verificado' in session:
        if session['verificado']:
            return redirect(url_for('home'))

    if request.method == 'POST':
        # Create variables for easy access
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        nombrecompleto = request.form['nombrecompleto']
        email = request.form['email']
        key = read_key_from_file('config.ini')
        _contraseñaHasheada = encrypt_text(contrasena, key)
        print(_contraseñaHasheada)
        # Verifica si el usuario existe en la base de datos
        cuenta = verificar_usuario(usuario)
        correoVerificar = verificar_correo(email)
        # Si la cuenta existe en la base de datos
        if cuenta:
            flash('La cuenta ya existe!')
        elif correoVerificar:
            flash('El correo ya existe en el sistema!')
        elif not re.match(r'[A-Za-z0-9]+', usuario):
            flash('El nombre de usuario debe contener solo caracteres y números!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Correo invalido!')
        elif not usuario or not contrasena or not email:
            flash('Por favor rellena el formulario!')
        else:
            # La cuenta no existe y los datos del formulario son válidos, ahora inserte una nueva cuenta en la tabla de usuarios
            estado_creacion = crear_usuario(
                nombrecompleto, usuario, _contraseñaHasheada, email)
            if estado_creacion:
                flash('Cuenta creada satisfactoriamente!')
            else:
                flash('Error al crear la cuenta!')

    # Muestra el formulario de registro con el mensaje (si existe)
    return render_template('register.html')


def iniciar_sesion():

    if 'verificado' in session:
        if session['verificado']:
            return redirect(url_for('home'))

    # Verifica si el usuario existe en la base de datos
    if request.method == 'POST' and 'usuario' in request.form and 'contrasena' in request.form:
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        # Verifica si el usuario existe en la base de datos
        cuenta = verificar_usuario(usuario)
        print(cuenta)
        # Si la cuenta existe en la base de datos
        if cuenta:
            contrasena_rs = cuenta['contrasena']
            # Verifica si la contraseña es correcta
            key = read_key_from_file('config.ini')
            if contrasena == decrypt_text(contrasena_rs, key):
                # Crear sesion
                session['logeado'] = True
                session['id'] = cuenta['id']
                session['usuario'] = cuenta['usuario']
                session['verificado'] = False
                session['otp'] = ''
                # Redirecciona a la pagina de inicio
                # return redirect(url_for('home'))
                # Redirecciona a la pagina de verificacion de otp
                return redirect(url_for('otp'))
            else:
                #  Contraseña incorrecta
                flash('Nombre de usuario/contraseña incorrectos')
        else:
            #  Usuario no existe
            flash('Nombre de usuario/contraseña incorrectos')

    return render_template('login.html')


def cerrar_sesion():
    # Eliminar sesion
    session.pop('logeado', None)
    session.pop('id', None)
    session.pop('usuario', None)
    session.pop('verificado', None)
    session.pop('otp', None)
    # Redirecciona a la pagina de inicio
    return redirect(url_for('home'))


def verificar_otp():
    if request.method == 'POST':
        otp = request.form['otp']
        if otp == session['otp']:
            session['verificado'] = True
            return redirect(url_for('home'))
        else:
            flash('Codigo OTP incorrecto')
            cerrar_sesion()

    else:
        if 'logeado' in session:
            # Se obtiene la cuenta del usuario
            cuenta = verificar_usuario(session['usuario'])
            codigo_otp = enviar_correo_otp(cuenta['email'])
            session['otp'] = codigo_otp
            print(codigo_otp)
            # Muestra la pagina de inicio con la informacion de la cuenta
            return render_template('otp.html', account=cuenta)
        # Usuario no esta logueado redirecciona a la pagina de inicio de sesion
    return redirect(url_for('login'))


def pag_home():
    if 'verificado' in session:
        # Si no es valido el otp lo regresa a la pagina de inicio
        if not session['verificado']:
            cerrar_sesion()
            return redirect(url_for('login'))

    if 'logeado' in session:
        # Se obtiene la cuenta del usuario
        cuenta = verificar_usuario(session['usuario'])
        # Muestra la pagina de inicio con la informacion de la cuenta
        return render_template('index.html', account=cuenta)
    # Usuario no esta logueado redirecciona a la pagina de inicio de sesion
    return redirect(url_for('login'))

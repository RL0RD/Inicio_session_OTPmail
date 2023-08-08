import pyotp
import smtplib
from email.mime.text import MIMEText
from .configuracion import get_config

# Obtén la configuración
config = get_config()

def generar_codigo_otp():
    # Genera una clave secreta aleatoria en base32
    clave_secreta = pyotp.random_base32()

    # Crea un objeto TOTP usando la clave secreta
    totp = pyotp.TOTP(clave_secreta)

    # Genera el código OTP actual basado en el objeto TOTP
    codigo_otp = totp.now()

    # Devuelve el código OTP generado
    return codigo_otp

def enviar_correo(remitente, destinatario, clave, titulo, mensaje):
    try:
        # Creación del objeto MIMEText con el contenido del mensaje
        correo = MIMEText(mensaje)

        # Establecer el remitente, destinatario y título del correo
        correo["From"] = remitente
        correo["To"] = destinatario
        correo["Subject"] = titulo

        # Establecer la conexión con el servidor SMTP de Gmail
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()

        # Iniciar sesión en la cuenta de correo con el remitente y clave
        smtp.login(remitente, clave)

        # Envío del correo electrónico
        smtp.sendmail(remitente, destinatario, correo.as_string())

        # Cerrar la conexión SMTP
        smtp.quit()

        # Imprimir mensaje de éxito
        print("Correo enviado correctamente")
    except Exception as e:
        # Manejar excepciones e imprimir mensaje de error
        print(f"Error al enviar el correo: {e}")


def enviar_correo_otp(correo):
    remitente = config['mail_username']
    clave = config['mail_password']
    destinatario = correo
    titulo = "Código OTP"
    codigo = generar_codigo_otp()
    mensaje = f"Hola, este es tu código OTP: {codigo}"
    enviar_correo(remitente, destinatario, clave, titulo, mensaje)
    return codigo

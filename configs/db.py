from .configuracion import get_config
import psycopg2
import psycopg2.extras
# Obtén la configuración
config = get_config()

def create_postgresql_connection():
    conn = psycopg2.connect(
        host=config['db_host'],
        port=config['db_port'],
        database=config['db_database'],
        user=config['db_username'],
        password=config['db_password']
    )
    return conn

def verificar_usuario(p_user):
    try:
        conexion = create_postgresql_connection()
        cursor = conexion.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = f"SELECT * FROM registro_usuarios WHERE usuario = %s"
        cursor.execute(query, (p_user,))
        resultado = cursor.fetchone()
        cursor.close()
    finally:
        conexion.close()
    return resultado if resultado else None

def verificar_correo(p_email):
    try:
        conexion = create_postgresql_connection()
        cursor = conexion.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = f"SELECT * FROM registro_usuarios WHERE email = %s"
        cursor.execute(query, (p_email,))
        resultado = cursor.fetchone()
        cursor.close()
    finally:
        conexion.close()
    return resultado if resultado else None

def crear_usuario(nombrecompleto, usuario, contrasena, email):
    try:
        conexion = create_postgresql_connection()
        cursor = conexion.cursor()
        query = "INSERT INTO registro_usuarios (nombrecompleto, usuario, contrasena, email) VALUES (%s, %s, %s, %s)"
        valores = (nombrecompleto, usuario, contrasena, email)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return False
    finally:
        conexion.close()
    
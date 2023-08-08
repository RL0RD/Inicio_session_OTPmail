from cryptography.fernet import Fernet
import configparser
import hashlib

# Función que genera el hash de un texto dado
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Función que cifra un texto dado
def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

# Función que descifra un texto dado
def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    return f.decrypt(encrypted_text.encode()).decode()

# Función que genere y grabe en un archivo el key para el aplicativo
def generate_key_file(key_filename):
    key = Fernet.generate_key()
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'key': key.decode()}
    with open(key_filename, 'w') as f:
        config.write(f)
    return key

# Función que lea el key para el aplicativo de un archivo .ini
def read_key_from_file(key_filename):
    config = configparser.ConfigParser()
    config.read(key_filename)
    return config['DEFAULT']['key'].encode()

# Ejemplo de uso
if __name__ == '__main__':
    print(generate_hash("hola"))
    # Generar y guardar la key en un archivo .ini
    # key = generate_key_file('config.ini')
    # print('Key generada y guardada en archivo key.ini')

    # Leer la key desde un archivo .ini
    key = read_key_from_file('config.ini')

    # Ejemplo de cifrado y descifrado de texto
    texto_original = 'Texto original'
    texto_cifrado = encrypt_text(texto_original, key)
    # texto_cifrado = 'gAAAAABkZZ4_-wj-2G5D9S6JnnxpyQ3feo6G0TVZrVd44AkkAOlhZb8igkTGi9h0ZW62eeTQCDGQYqNGvU75Z6a3zFFOsCx-xg=='
    texto_descifrado = decrypt_text(texto_cifrado, key)

    print('Texto original:', texto_original)
    print('Texto cifrado:', texto_cifrado)
    print('Texto descifrado:', texto_descifrado)

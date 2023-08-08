import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Crea un diccionario con las variables de configuración
    config_dict = {
        'key': config.get('DEFAULT', 'KEY'),

        'mail_username': config.get('DEFAULT', 'MAIL_USERNAME'),
        'mail_password':config.get('DEFAULT', 'MAIL_PASSWORD'),

        'db_host': config.get('DEFAULT', 'DB_HOST'),
        'db_port': config.get('DEFAULT', 'DB_PORT'),
        'db_database': config.get('DEFAULT', 'DB_DATABASE'),
        'db_username': config.get('DEFAULT', 'DB_USERNAME'),
        'db_password': config.get('DEFAULT', 'DB_PASSWORD'),
    }

    return config_dict

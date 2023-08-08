# Inicio_session_OTPmail

Basado en una arquitectura modular, donde se prioriza la implementación de medidas prácticas para salvaguardar la integridad de los datos de los usuarios. En particular, se ha prestado una atención especial al tratamiento seguro de información altamente sensible, como es el caso de las contraseñas de los usuarios. Estas contraseñas son sometidas a un proceso de validación basado en su función hash en lugar de una comparación directa de caracteres en texto plano. Esta metodología se adopta con el objetivo de evitar la exposición de las contraseñas en caso de que un atacante intercepte el tráfico de red, ya sea en el entorno del usuario o en una infraestructura corporativa.

La utilización de funciones hash en este contexto implica que, en lugar de almacenar o transmitir las contraseñas en su forma original, se emplea una representación criptográfica irreversible generada por la función hash. Esto contribuye a una mayor seguridad, ya que el hash resultante no revela directamente la contraseña original y dificulta significativamente la tarea de descifrar su valor. Además, este enfoque minimiza el riesgo de que se revelen patrones o similitudes entre contraseñas, ya que incluso contraseñas similares pueden generar hashes considerablemente diferentes. 

Lenguajes utilizados
- SQL
- PYTHON

Librerias y frameworks destacadas
- Asgiref
- Cryptography
- Django
- Flask

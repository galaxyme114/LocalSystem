# LocalSystem

# Tecnologias usadas para este proyecto

  Django 2.2.6, Python >3.5.3, Bootstrap 4.3.1 y jquery 3.3.1

# Instalación

prerequisitos

* pip:

  instalamos pip3 metodo get pip

  sudo apt-get install curl

  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

  sudo python3 get-pip.py

* virtualenv (opcional):

  Instalar virtualenv

  sudo apt-get install python-virtualenv virtualenv

  Comando para ver ruta de nuestro interprete python:

  which python3

  Comando para crear entorno virtual:

  virtualenv nombre_de_mi_entorno -p /usr/bin/python3

  Comando para activar el entorno:

  source nombre_de_mi_entorno/bin/activate

  Comando para desactivar el entorno:

  deactivate

1.Entrar a la carpeta LocalSystem.

    cd LocalSystem

2.Instalar dependencias con pip. (Si estas usando entorno virtual recuerda activarlo)

    pip install -r requirements.txt

3.Realizar las migraciones

    python manage.py makemigrations

    o hacer las migraciones por separado en caso de que no falle el comando 
    
    python manage.py makemigrations cities_light
    python manage.py makemigrations part

    y por ultimo crear la base de datos

    python manage.py migrate
    
    python manage.py loaddata System/part/data/users.json
    python manage.py loaddata System/part/data/ivas.json
    python manage.py loaddata System/part/data/taxrate.json

    python manage.py cities_light --force-all

4.Correr el proyecto:

    python manage.py runserver


    username: admin
    password: medcombo123



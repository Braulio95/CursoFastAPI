import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" se guarda el nombre de la base de datos"""
sqlitefilename = "../database.sqlite"

""" lee el directorio actual de la base de datos, se importa del modulo os"""
basedir = os.path.dirname(os.path.realpath(__file__))

""" ruta final de la conexión a la base de datos"""
databaseurl = f"sqlite:///{os.path.join(basedir, sqlitefilename)}"

""" representa el motor de la base de datos, el comando echo true muestra en consola lo que se realiza, se importa el metodo create engine de sqlalchemy"""
engine = create_engine(databaseurl, echo=True)

"""Se crea session para conectar a la base de datos, se enlaza al comando bind y se iguala a engine"""
Session = sessionmaker(bind=engine)
#Se utiliza para manipular la base de datos
Base = declarative_base()
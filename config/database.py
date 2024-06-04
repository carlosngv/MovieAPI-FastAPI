import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__)) # ? Referencia al directorio actual de este archivo

db_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

engine = create_engine(db_url, echo=True) # ? Echo muestra por consola lo que realiza la base de datos

# ? Sesión para conectarme a la db
Session = sessionmaker(bind=engine)

# ? declarative_base para manipular las tablas
Base = declarative_base()

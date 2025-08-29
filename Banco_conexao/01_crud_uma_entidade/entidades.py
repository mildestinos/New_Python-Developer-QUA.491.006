# entidades.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

# Base declarativa
Base = declarative_base()

# Definição da Entidade
class Pessoa(Base):
    __tablename__ = "pessoa"

    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    data_nasc = Column(Date, nullable=False)

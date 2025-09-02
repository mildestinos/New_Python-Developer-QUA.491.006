from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

# Criação do objeto Base
Base = declarative_base()

# Definição da entidade Pessoa
class Pessoa(Base):
    __tablename__ = 'pessoa'

    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    data_nasc = Column(Date, nullable=True)

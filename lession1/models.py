"""
    Model
"""
from sqlalchemy import Column, Integer, String
from database import Base, engine

# Model ORM
class Account(Base):
    """
        Model of account
    """
    __tablename__ = "accounts"

    registerID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)
    phone = Column(String(20), nullable=False)

Base.metadata.create_all(bind=engine)
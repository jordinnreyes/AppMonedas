# models/transaccion.py

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Transaccion(Base):
    __tablename__ = "transacciones"
    
    id = Column(Integer, primary_key=True)
    origen_usuario_id = Column(Integer, nullable=False)
    destino_usuario_id = Column(Integer, nullable=False)

    monto_origen = Column(Float, nullable=False)
    monto_convertido = Column(Float, nullable=False)
    moneda_origen = Column(String, nullable=False)
    moneda_destino = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"))  # Asume relación con User
    
    usuario = relationship("User")

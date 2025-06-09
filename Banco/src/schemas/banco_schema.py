from pydantic import BaseModel, Field
from typing import Literal

class TransaccionRequest(BaseModel):
    origen: str
    destino: str
    monto: float = Field(..., gt=0)
    moneda_origen: Literal["USD", "EUR", "PEN"]
    moneda_destino: Literal["USD", "EUR", "PEN"]

class TransaccionResponse(BaseModel):
    origen: str
    destino: str
    monto_origen: float
    monto_convertido: float
    moneda_destino: str

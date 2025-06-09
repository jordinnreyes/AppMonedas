from fastapi import APIRouter, HTTPException
from ..schemas.banco_schema import TransaccionRequest, TransaccionResponse
from ..services.banco_service import procesar_transaccion

router = APIRouter()

@router.post("/transaccion", response_model=TransaccionResponse)
async def crear_transaccion(data: TransaccionRequest):
    try:
        return await procesar_transaccion(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

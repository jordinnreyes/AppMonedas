from fastapi import APIRouter, HTTPException
from ..services.cambio_service import get_exchange_rate

router = APIRouter(prefix="/exchange", tags=["exchange"])

@router.get("/")
async def convert_currency(base: str, target: str, amount: float):
    try:
        rate = await get_exchange_rate(base.upper(), target.upper())
        converted = amount * rate
        return {
            "base": base.upper(),
            "target": target.upper(),
            "rate": rate,
            "amount": amount,
            "converted": round(converted, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

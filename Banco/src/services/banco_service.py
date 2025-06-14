import httpx
from ..schemas.banco_schema import TransaccionRequest, TransaccionResponse

CAMBISTA_URL = "http://cambista:8000/cambio/exchange/"


async def procesar_transaccion(data: TransaccionRequest) -> TransaccionResponse:
    if data.moneda_origen == data.moneda_destino:
        monto_convertido = data.monto
    else:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                CAMBISTA_URL,
                params={"amount": data.monto, "base": data.moneda_origen, "target": data.moneda_destino}
            )
            if response.status_code != 200:
                raise Exception("Error al convertir moneda")
            monto_convertido = response.json()["converted"]

    return TransaccionResponse(
        origen=data.origen,
        destino=data.destino,
        monto_origen=data.monto,
        monto_convertido=monto_convertido,
        moneda_destino=data.moneda_destino
    )


#POST /banco/transaccion
#{
#  "origen": "Cuenta123",
#  "destino": "Cuenta456",
#  "monto": 100,
#  "moneda_origen": "USD",
#  "moneda_destino": "EUR"
#}
#
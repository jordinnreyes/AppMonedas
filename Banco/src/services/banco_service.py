import httpx
from ..schemas.banco_schema import TransaccionRequest, TransaccionResponse
from ..config.settings import settings  # importa tu configuración

CAMBISTA_URL = "http://cambista:8000/cambio/exchange/"

USUARIOS_URL = settings.USUARIOS_SERVICE_URL


async def validar_usuario(usuario_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USUARIOS_URL}/users/users/{usuario_id}")
        if response.status_code != 200:
            raise Exception(f"Usuario {usuario_id} no encontrado")
        return response.json()

async def procesar_transaccion(data: TransaccionRequest) -> TransaccionResponse:

    # Validar usuarios origen y destino
    origen_data = await validar_usuario(data.origen_usuario_id)
    destino_data = await validar_usuario(data.destino_usuario_id)

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
        origen_usuario_id=origen_data["id"],          #  solo el id
        destino_usuario_id=destino_data["id"],
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
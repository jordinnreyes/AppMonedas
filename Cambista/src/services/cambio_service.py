import httpx
from ..config.settings import settings

async def get_exchange_rate(base: str, target: str):
    url = f"{settings.CURRENCY_API_URL}?apikey={settings.CURRENCY_API_KEY}&base_currency={base}&currencies={target}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print("Respuesta cruda:", data)
        if response.status_code != 200:
            raise Exception(data.get("message", "Error en API externa"))

        return data["data"][target]

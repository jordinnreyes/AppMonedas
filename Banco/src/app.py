from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .controllers import transaccion_controller

app = FastAPI(
    title="Servicio Banco",
    description="Servicio de transacciones entre cuentas con soporte para múltiples monedas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(transaccion_controller.router, prefix="/banco", tags=["banco"])

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "message": "Servicio banco operativo"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

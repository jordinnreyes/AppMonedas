from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .controllers import cambio_controller

app = FastAPI(
    title="Servicio Cambista",
    description="API para obtener tasas de cambio usando FreeCurrencyAPI",
    version="1.0.0"
)

# Middleware CORS (ajusta en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a dominios seguros en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(cambio_controller.router, prefix="/cambio", tags=["cambio"])

# Endpoint de salud
@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "message": "Servicio cambista operativo"}

# Manejo global de errores
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

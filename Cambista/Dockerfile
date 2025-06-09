FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema (más liviano porque no usamos psycopg2 aquí)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Configurar PYTHONPATH si tu código está en src/
ENV PYTHONPATH=/app/src

# Comando de arranque
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
#el requiremets :Como este microservicio no usa base de datos 
#ni autenticación, solo necesitas dependencias para FastAPI, requests y entorno:
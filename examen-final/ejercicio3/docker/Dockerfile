# Stage 1: Build
FROM alpine:3.14 AS builder
WORKDIR /build
# Copiamos el archivo requirements.txt
COPY ../app/requirements.txt .
# Instalamos dependencias
RUN apk add --no-cache python3 py3-pip
RUN pip install -r requirements.txt

# Copiamos el resto de la aplicación
COPY ../app .
RUN echo "Build finalizado"

# Stage 2: Production (Optimizado)
FROM alpine:3.14
WORKDIR /app
# Instalamos python, pip y curl
RUN apk add --no-cache python3 py3-pip curl
# Copiamos las dependencias de python
COPY --from=builder /usr/lib/python3.9/site-packages/ /usr/lib/python3.9/site-packages/
# Copiamos el resto de la aplicación
COPY --from=builder /build .
# Corremos la aplicación
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
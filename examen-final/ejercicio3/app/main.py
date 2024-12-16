from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "¡Hola profe! Este es el ejercicio 3"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

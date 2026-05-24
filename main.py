from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.unidad import router as unidad_router

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================
# ROUTERS
# =========================

app.include_router(unidad_router)

# =========================
# INICIO
# =========================

@app.get("/")
def inicio():

    return {
        "mensaje": "API funcionando correctamente"
    }
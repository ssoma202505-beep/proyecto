from fastapi import APIRouter

from schemas.unidad_schema import UnidadSchema

from services.unidad_service import (

    listar_unidades,
    insertar_unidad,
    actualizar_unidad,
    eliminar_unidad
)

router = APIRouter()

# =========================
# GET
# =========================

@router.get("/unidad")
def get_unidades():

    return listar_unidades()


# =========================
# POST
# =========================

@router.post("/unidad")
def post_unidad(unidad: UnidadSchema):

    insertar_unidad(unidad.descripcion)

    return {
        "ok": True,
        "mensaje": "Unidad insertada"
    }


# =========================
# PUT
# =========================

@router.put("/unidad/{id}")
def put_unidad(id: int, unidad: UnidadSchema):

    actualizar_unidad(
        id,
        unidad.descripcion
    )

    return {
        "ok": True,
        "mensaje": "Unidad actualizada"
    }


# =========================
# DELETE
# =========================

@router.delete("/unidad/{id}")
def delete_unidad(id: int):

    eliminar_unidad(id)

    return {
        "ok": True,
        "mensaje": "Unidad eliminada"
    }
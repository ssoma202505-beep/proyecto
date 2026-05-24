from pydantic import BaseModel, Field

class UnidadSchema(BaseModel):

    descripcion: str = Field(
        min_length=2,
        max_length=100
    )
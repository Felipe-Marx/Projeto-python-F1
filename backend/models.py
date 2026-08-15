from pydantic import BaseModel, Field, field_validator

class DriverCreate(BaseModel):
    name: str = Field(min_length=1)
    team: str = Field(min_length=1)
    points: int = Field(ge=0)

    @field_validator("name", "team")
    @classmethod
    def verificar_texto(cls, texto:str):
        if not texto.strip():
            raise ValueError("Nome ou Time inválido.")
        return texto.strip()
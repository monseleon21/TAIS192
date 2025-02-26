from pydantic import BaseModel, Field, EmailStr

#modelo
class ModeloUsuario(BaseModel):
    id:int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre:str = Field(..., min_length=3, max_length=85, description="Solo letras min: 3 max 85")
    edad:int = Field(..., gt=0, ge=121, description="Solo edad mayor a: 0  menor a: 121")
    correo: EmailStr = Field(..., description="Solo correos con estructura: example@example.com")

from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title='Mi primera API 192',
    description='Maria Monserrat Campuzano Leon',
    version='1.0.1'
)

# Lista de usuarios
usuarios = [
    {"id": 1, "nombre": "monchis", "edad": 22},
    {"id": 2, "nombre": "alejandro", "edad": 24},
    {"id": 3, "nombre": "maria", "edad": 20},
    {"id": 4, "nombre": "felix", "edad": 23}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint promedio
@app.get('/promedio', tags=['Promedios'])
def promedio():
    return 5.5

# Endpoint parámetro obligatorio
@app.get('/usuario/{id}', tags=['Parámetro obligatorio'])
def consulta_usuario_obligatorio(id: int):
    for usu in usuarios:
        if usu["id"] == id:
            return {"mensaje": "Usuario encontrado", "usuario": usu}
    return {"mensaje": f"No se encontró el usuario con el id: {id}"}


# Endpoint parámetro opcional
@app.get('/usuario/opcional/', tags=['Parámetro Opcional'])
def consulta_usuario_opcional(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usu}
        return {"mensaje": f"No se encontró el usuario con el id: {id}"}
    else:
        return {"mensaje": "No se proporcionó un ID"} 

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
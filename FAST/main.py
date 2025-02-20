from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(
    title='Mi primera API 192',
    description='Maria Monserrat Campuzano Leon',
    version='1.0.1'
)

#modelo
class ModeloUsuario(BaseModel):
    id:int
    nombre:str
    edad:int
    correo:str

#BD ficticia
usuarios = [
    {"id": 1, "nombre": "monchis", "edad": 22, "correo": "example@example.com"},
    {"id": 2, "nombre": "alejandro", "edad": 24, "correo": "example2@example.com"},
    {"id": 3, "nombre": "maria", "edad": 20,"correo": "example3@example.com"},
    {"id": 4, "nombre": "felix", "edad": 23, "correo": "example4@example.com"}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

#Enpoint CONSULTA TODDOS
@app.get('/todoUsuarios' ,response_model= List[ModeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuario():
  return {"Los usuarios registrados son": usuarios}

""" # Endpoint CONSULTA TODOS
@app.get('/todoUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
  return {"Los usuarios registrados son": usuarios}
 """
# Endpoint Agregar Usuarios Post
@app.post('/usuario', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
        
    usuarios.append(usuario)
    return usuario

# Endpoint para actualizar PUT
@app.put('/usuario/{user_id}', tags=['Operaciones CRUD'])
def actualizarUsuario(user_id: int, usuario_actualizado: dict):
    for i, usr in enumerate(usuarios):
        if usr["id"] == user_id:
            usuarios[i].update(usuario_actualizado) 
            return {"mensaje": "Usuario actualizado correctamente", "usuario": usuarios[i]}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint Agregar Usuarios DELETE
@app.delete('/usuario/{user_id}', tags=['Operaciones CRUD'])
def deleteUsuario(user_id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == user_id:
            usuarios.pop(index)
            return{"mensaje":"Usuario eliminado correctamente"}
        else:
             raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
                
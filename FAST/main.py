from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import ModeloUsuario

app = FastAPI(
    title='Mi primera API 192',
    description='Maria Monserrat Campuzano Leon',
    version='1.0.1'
)


#BD ficticia
usuarios = [
    {"id": 1, "nombre": "monchis", "edad": 22, "correo": "example@example.com"},
    {"id": 2, "nombre": "alejandro", "edad": 24, "correo": "example2@example.com"},
    {"id": 3, "nombre": "maria", "edad": 20, "correo": "example3@example.com"},
    {"id": 4, "nombre": "felix", "edad": 23, "correo": "example4@example.com"}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

#Enpoint CONSULTA TODDOS
@app.get('/todoUsuarios' ,response_model= List[ModeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuario():
  return usuarios

# Endpoint Agregar Usuarios Post
@app.post('/usuario/', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:ModeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El id ya existe")
   
    usuarios.append(usuario)
    return usuario


# Endpoint para actualizar PUT
@app.put('/usuario/{id}', response_model=ModeloUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: ModeloUsuario):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[i]= usuarioActualizado.model_dump()
            return usuarios[i]
    
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
    
                
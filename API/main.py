from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI()



#Lita de tareas 
tareas =[
    {"id": 1, "titulo": "Leer", "descripcion": "La Alargada sombra del amor", "vencimiento": "10-10-25", "estado": "completada"},
    {"id": 2, "titulo": "Estudiar", "descripcion": "Examen de SO", "vencimiento": "11-11-25", "estado": "no completada"},
    {"id": 3, "titulo": "Lavar mi ropa", "descripcion": "Tengo toda la semana", "vencimiento": "12-02-25", "estado": "completada"},
    {"id": 4, "titulo": "Actualizar", "descripcion": "Actualizar mi computadora", "vencimiento": "15-04-25", "estado": "no completada"},
    {"id": 5, "titulo": "Hacer mi tarea", "descripcion": "tarea de investigacion de reingieneria", "vencimiento": "24-03-25", "estado": "completada"}
]

#Endpoit home 
@app.get('/', tags=['Hola mundo'])
def home():
    return {'hello': 'world API TAREA'}


#Endpoint get obetener todas las tareas
@app.get('/todoTareas', tags=['Lista de Tareas'])
def leerTareas():
    return{"Las tareas pendientes son estas": tareas}
    

#Endpoint buscar por ID
@app.get('/tareas/{tareas_id}', tags=['Lista de Tareas'])
def obtenerTareas(tareas_id: int):
    for ta in tareas:
        if ta["id"] == tareas_id:
            return {"La tarea encontrada es": ta}
    raise HTTPException(status_code=404, detail="No se encontró la tarea")

#Endpoint Crear una nueva tarea
@app.post('/tareas', tags=['Lista de Tareas'])
def crearTarea(tarea:dict):
    for ta in tareas:
        if ta ["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail= "El id de esa tarea ya existe, agregue otro ID")
    tareas.append(tarea)
    return tarea
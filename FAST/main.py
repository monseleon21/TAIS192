from fastapi import FastAPI #importacion

app= FastAPI() #creamos objeto app tipo FastAPI

#Creamos Endpoint home
@app.get('/') #tipo get que se atiende cuando arrannca el inicio,
def home(): #  y trabajara con nuna funcion home  
    return {'hello':'world FastAPI'} # y va a regresar un elemento que tenga un Hola mundo 
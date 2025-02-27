import jwt
def createToken(datos: dict):
    token:str= jwt.encode(payload=datos, key='secretkey', algorithm='HS256') #ponemos los parametros que ocupa son 3
    return token
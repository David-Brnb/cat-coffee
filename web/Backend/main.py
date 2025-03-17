from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
import bcrypt
import os

app = FastAPI()

# Ruta correcta de la base de datos
DB_PATH = "C:/Users/Alan2/OneDrive/Documentos/GitHub/cat-coffee/web/Backend/cat_cafe.db"


# Modelo de datos para el login
class LoginRequest(BaseModel):
    usuario: str
    contrasena: str

# Función para obtener conexión a la base de datos
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Función para encriptar contraseñas con bcrypt
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# Endpoint para validar usuario
@app.post("/login")
def validar_usuario(data: LoginRequest):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario=?", (data.usuario,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(data.contrasena.encode("utf-8"), user["contrasena"].encode("utf-8")):
        return {"message": "Login exitoso"}
    
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# Endpoint para obtener el menú
@app.get("/menu")
def obtener_menu():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM platillos")
    platillos = cursor.fetchall()
    return [dict(row) for row in platillos]

# Endpoint para obtener información de los gatos
@app.get("/gatos")
def obtener_gatos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gatos")
    gatos = cursor.fetchall()
    return [dict(row) for row in gatos]

# Endpoint para obtener imágenes de gatos (ruta)
@app.get("/imagen_gato/{id}")
def obtener_imagen_gato(id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ruta_foto FROM gatos WHERE id=?", (id,))
    gato = cursor.fetchone()
    if gato:
        return {"ruta_foto": gato["ruta_foto"]}
    
    raise HTTPException(status_code=404, detail="Imagen no encontrada")


@app.get("/imagen_platillo/{id}")
def obtener_imagen_platillo(id: int):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT ruta_foto FROM platillos WHERE id=?", (id,))
    platillo = cursor.fetchone()
    
    conn.close()

    if platillo:
        return {"ruta_foto": platillo[0]}  # Accede correctamente al valor

    raise HTTPException(status_code=404, detail="Imagen no encontrada")
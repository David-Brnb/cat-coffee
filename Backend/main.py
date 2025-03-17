from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
import bcrypt
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Ruta correcta de la base de datos
DB_PATH = "cat_cafe.db"

# Modelo de datos para el login
class LoginRequest(BaseModel):
    usuario: str
    contrasena: str

class RegisterRequest(BaseModel):
    usuario: str
    contraseña: str


# Función para obtener conexión a la base de datos
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

SALT = bcrypt.gensalt(rounds=12) 

# Función para encriptar contraseñas con bcrypt
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), SALT).decode("utf-8")


# Configuración de CORS para aceptar todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceptar todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Endpoint para validar usuario
@app.post("/login")
def validar_usuario(data: LoginRequest):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario=?", (data.usuario,))
    user = cursor.fetchone()

    print(hash_password(data.contraseña))
    print(user["contraseña"])

    if user and hash_password(data.contraseña) == user["contraseña"]:
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

@app.post("/register")
def registrar_usuario(data: RegisterRequest):
    conn = get_db()
    cursor = conn.cursor()

    # Verificar si el usuario ya existe
    cursor.execute("SELECT usuario FROM usuarios WHERE usuario=?", (data.usuario,))
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Hashear la contraseña
    hashed_password = hash_password(data.contraseña)
    print(hashed_password)

    # Insertar nuevo usuario
    cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", 
                   (data.usuario, hashed_password))
    conn.commit()
    conn.close()

    return {"message": "Registro exitoso"}
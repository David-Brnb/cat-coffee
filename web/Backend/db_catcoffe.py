import sqlite3
import hashlib

# hash para contraseñas :)
def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def create_database():

    conn = sqlite3.connect('cat_cafe.db', check_same_thread=False)
    cursor = conn.cursor()

    #  tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ruta_foto TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS platillos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        descripcion TEXT,
        categoria TEXT,
        ruta_foto TEXT NOT NULL
    )
    ''')

    #  datos de ejemplo

    usuarios = [
        ('usuario_admin', hash_password('admin123')),
        ('usuario1', hash_password('pass1234')),
        ('usuario2', hash_password('securepass')),
        ('usuario4', hash_password('pass_test')),
        ('usuario5', hash_password('password1234'))
    ]

    cursor.executemany('INSERT OR IGNORE INTO usuarios (usuario, contraseña) VALUES (?, ?)', usuarios)


    gatos = [
        ('Michi', 'https://t4.ftcdn.net/jpg/00/91/65/23/360_F_91652321_TPJIx4LRRlp3rMLdzLDF1xlRb2ghjSd2.jpg', 'Aunque no lo creas, sí, así se llama, digamos que el dueño del lugar no fue muy creativo al nombrarlo, ya que cuando este amigo llego con nosotros, este establecimiento apenas estaba empezando, es el abuelito que todos quieren.'),
        ('Centauri', 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/75/d9/e8/this-is-johnny-a-sweet.jpg?w=1200&h=-1&s=1', 'Técnicamente, Centauri no es un gato, pero aun así lo queremos y es muy tranquilo.'),
        ('Goobert', 'https://t3.ftcdn.net/jpg/07/06/89/92/360_F_706899227_XaK3lLcx3moA4jQXhNe4ubCTlRyUJoT4.jpg', 'Simplemente Goobert, existe y ya, ningun pensamiento pasa por su cabeza (aunque creemos que es capaz de colapsar el gobierno).'),
        ('Andromeda', 'https://i.cbc.ca/1.3226364.1442241715!/fileImage/httpImage/image.JPG_gen/derivatives/original_620/cat-cafe.JPG', 'Andrómeda está siempre muy cerca de ti, es simplemente alguien curiosa a sus 2 años que puede pasar un tiempo divertido y lleno de actividades .'),
        ('Milky-Way', 'https://media.istockphoto.com/id/1164498663/photo/autumn-cozy-composition-with-ginger-cat.jpg?s=612x612&w=0&k=20&c=gs7ofZZsvzF2_CLGKKKI2GPWqOKfembeesD-JG8KRew=', 'Milky-way, la verdad es que es tu mejor compañero si lo que te encanta destruir cosas, según nuestros contadores ya debe 2000 en gastos de juguetes.')
    ]

    cursor.executemany('INSERT OR IGNORE INTO gatos (nombre, ruta_foto, descripcion) VALUES (?, ?, ?)', gatos)


    platillos = [
        ('Café Latte', 60.00, 'Espresso con leche caliente y una pequeña capa de espuma', 'Bebidas',"latte.jpg"),
        ('Pastel de Chocolate', 90.00, 'Pastel de chocolate con decoración de huella de gato', 'Postres',"pastel.jpg"),
        ('pasta a pomodoro', 120.00, 'Pasta de su eleccion preparada en salsa pomodoro', 'Comidas',"pomodoro.jpg"),
        ('Jugo de carne', 150.00, 'Plato grande de jugo de carne acompañado de tostadas de tuetano', 'Comidas',"jugo.jpg"),
        ('Té Chai', 40.00, 'Té negro con especias y leche', 'Bebidas',"chai"),
        ('Galletas Galacticas', 60.00, 'Galletas caseras de mantequilla ', 'Snacks',"galletas.jpg"),
        ('Meow-chiato', 60, 'Machiato con espuma decorada', 'Bebidas',"chiato.jpg"),
        ('Alimenta a los patrones', 100, 'Plato de comida a base de croquetas y salmon calientito', 'alimento para gatos',"patrones.jpg")
    ]

    cursor.executemany('INSERT OR IGNORE INTO platillos (nombre, precio, descripcion, categoria, ruta_foto) VALUES (?, ?, ?, ?, ?)', platillos)



    conn.commit() 
    conn.close()



def validar_usuario(usuario, contraseña):
    conn = sqlite3.connect('cat_cafe.db')
    cursor = conn.cursor()

    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] == hash_password(contraseña):
        return True
    else:
        return False


def obtener_gatos():
    conn = sqlite3.connect('cat_cafe.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM gatos')
    gatos = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return gatos


def obtener_menu():
    conn = sqlite3.connect('cat_cafe.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM platillos')
    platillos = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return platillos


def obtener_imagen_gato(id_gato):
    conn = sqlite3.connect('cat_cafe.db')
    cursor = conn.cursor()

    cursor.execute('SELECT ruta_foto FROM gatos WHERE id = ?', (id_gato,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return resultado[0]
    else:
        return None
    
def obtener_imagen_platillo(id_platillo):
    conn = sqlite3.connect('cat_cafe.db')
    cursor = conn.cursor()

    cursor.execute('SELECT ruta_foto FROM platillos WHERE id = ?', (id_platillo,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return resultado[0]  # Retorna la URL de la imagen del platillo
    else:
        return None


#lil test :D
if __name__ == '__main__':

    create_database()

    print("Validación de usuario admin:", validar_usuario("admin", "admin123"))
    print("Lista de gatos:", obtener_gatos())
    print("Menú completo:", obtener_menu())
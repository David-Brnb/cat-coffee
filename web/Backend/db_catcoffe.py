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
        ('Michi', 'https://images.ctfassets.net/denf86kkcx7r/4IPlg4Qazd4sFRuCUHIJ1T/f6c71da7eec727babcd554d843a528b8/gatocomuneuropeo-97', 'Aunque no lo creas, sí, así se llama, digamos que el dueño del lugar no fue muy creativo al nombrarlo, ya que cuando este amigo llego con nosotros, este establecimiento apenas estaba empezando, es el abuelito que todos quieren.'),
        ('Centauri', 'https://es.onlyfresh.com/cdn/shop/articles/AManova_diarrea_nei_gatti.jpg?v=1643195698&width=1100.jpg', 'Técnicamente, Centauri no es un gato, pero aun así lo queremos y es muy tranquilo.'),
        ('Goobert', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUGHcJLzr_MKK-6WUSKY0wEjd0eof09OWvjw&s', 'Simplemente Goobert, existe y ya, ningun pensamiento pasa por su cabeza (aunque creemos que es capaz de colapsar el gobierno).'),
        ('Andromeda', 'https://okdiario.com/img/2020/07/25/curiosidades-sobre-la-inteligencia-de-los-gatos.jpg', 'Andrómeda está siempre muy cerca de ti, es simplemente alguien curiosa a sus 2 años que puede pasar un tiempo divertido y lleno de actividades .'),
        ('Milky-Way', 'https://okdiario.com/img/2022/10/18/los-gatos-pueden-ver-en-color-1.jpg', 'Milky-way, la verdad es que es tu mejor compañero si lo que te encanta destruir cosas, según nuestros contadores ya debe 2000 en gastos de juguetes.')
    ]

    cursor.executemany('INSERT OR IGNORE INTO gatos (nombre, ruta_foto, descripcion) VALUES (?, ?, ?)', gatos)


    platillos = [
        ('Café Latte', 60.00, 'Espresso con leche caliente y una pequeña capa de espuma', 'Bebidas',"https://cdn7.kiwilimon.com/recetaimagen/36986/640x640/46349.jpg.jpg"),
        ('Pastel de Chocolate', 90.00, 'Pastel de chocolate con decoración de huella de gato', 'Postres',"https://www.verybestbaking.com/sites/g/files/jgfbjl326/files/styles/large/public/recipe-thumbnail/103679-2020_06_09T08_18_01_mrs_ImageRecipes_1810lrg.jpg?itok=DR3HQYQ1"),
        ('pasta a pomodoro', 120.00, 'Pasta de su eleccion preparada en salsa pomodoro', 'Comidas',"https://www.placermonticello.com/cms/wp-content/uploads/placer_monticello_pasta_pomodoro.jpg"),
        ('Jugo de carne', 150.00, 'Plato grande de jugo de carne acompañado de tostadas de tuetano', 'Comidas',"https://www.unileverfoodsolutions.com.mx/dam/global-ufs/mcos/NOLA/calcmenu/recipes/MX-recipes/general/jugo-de-carne/1260x700_Jugo%20de%20carne.jpg"),
        ('Té Chai', 40.00, 'Té negro con especias y leche', 'Bebidas',"https://mccormick-cms.ext-sites-prd.cloudherdez.com/assets/d991ec67-15ec-41de-83e1-75ff779b7410"),
        ('Galletas Galacticas', 60.00, 'Galletas caseras de mantequilla ', 'Snacks',"https://i.pinimg.com/originals/71/a0/12/71a012b85a60f5f60a39a9cc502a4c4f.jpg"),
        ('Meow-chiato', 60, 'Machiato con espuma decorada', 'Bebidas',"https://previews.123rf.com/images/mrnovel/mrnovel1510/mrnovel151000020/47392237-arte-del-latte-del-caf%C3%A9-cara-del-gato-en-la-tabla.jpg"),
        ('Alimenta a los patrones', 100, 'Plato de comida a base de croquetas y salmon calientito', 'alimento para gatos',"https://cloudfront-us-east-1.images.arcpublishing.com/larazondemexico/FNCN2BTI6VGUXIPKPD34FQPFNQ.jpeg")
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
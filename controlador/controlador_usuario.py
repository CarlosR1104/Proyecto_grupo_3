from bd import obtener_conexion

def formulario_usuarios(correoUsua,username,password):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Usuario(correoUsua,username,password) VALUES (%s, %s, %s)",
                       (correoUsua,username,password))
    conexion.commit()
    conexion.close()


def listar_Producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombreProd, descripcionProd, url FROM producto")
        productos = cursor.fetchall()
    conexion.close()
    return productos 
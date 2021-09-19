from bd import obtener_conexion


def insertar_Producto(nombreProd, descripcionProd, url):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(nombreProd, descripcionProdc, url) VALUES (%s, %s, %s)",
                       (nombreProd, descripcionProd, url))
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


def eliminar_Productp(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def actualizar_Producto(nombreProd, descripcionProd,url):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombreProdu = %s, descripcionProd = %s, url = %s WHERE id = %s",
                       (nombreProd, descripcionProd,url))
    conexion.commit()
    conexion.close()






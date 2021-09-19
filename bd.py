import pymysql
#try:
def obtener_conexion():
	    return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='muebles_nalencia')
	   ## print("Conexión correcta")
#except (pymysql.err.OperationalError, pymysql.err.#InternalError) as e:
	#print("Ocurrió un error al conectar: ", e)
from flask import Flask, render_template, request, redirect, flash
from flask.templating import render_template_string
import controlador_producto 
import controlador_cliente
import controlador_usuario
app = Flask(__name__)

"""
Definición de rutas
"""
@app.route("/")
@app.route ("/muebles")
def muebles ():
    muebles = controlador_producto.listar_Producto()
    return render_template("muebles.html", muebles=muebles)


@app.route("")
def fomulario_usuario ():
    return render_template ("")


@app.route("/")
def formulario_agregra_mueble ():
    return render_template ("")


@app.route("/")
def guardar_mueble ():
    nombre= request.form ["nombre"]
    descripcion = request.form ["descripcion"]
    precio = request.form ["precio"]
    url = request.form ["url"]
    controlador_producto.insertar_producto (nombre,descripcion,precio,url)
    return render_template ("")


@app.route("")
def eliminar ():
    pass


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
import snappy
from snappy import Product
from snappy import ProductIO
from snappy import ProductUtils
from snappy import WKTReader
from snappy import HashMap
from snappy import GPF
# Para leer shapefiles
import shapefile
import pygeoif
import math
import tkinter as tk
#Popup windows
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry ("900x1000")

#Configurar color de fondo
ventana.config(bg="yellow")

#Configuracion de la primera fila y sus atributos
label_1 = tk.Label(ventana, text="1. Seleccionar una imagen", bg="yellow", fg="black", font = "Arial 15")
label_1.grid (row = 1, column = 1, pady=5)

boton_1 = tk.Button(text = "Escoger una imagen", font= 'Arial 13')##, command = parametros)
boton_1.grid(row = 3, column = 2, columnspan = 10, pady = 10)

cuadro_1 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_1.grid (row = 2, column = 2, pady = 10)

label_2 = tk.Label(ventana, text="2. Seleccionar un archivo ", bg="yellow", fg="black", font = "Arial 15")
label_2.grid (row = 4, column = 2, pady = 10)

boton_2 = tk.Button(text = "Escoger un archivo shapefile", font= 'Arial 13')##, command = parametros)
boton_2.grid(row = 6, column = 2, columnspan = 5, pady = 10)

cuadro_2 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_2.grid (row = 5, column = 2, pady = 10)

label_3 = tk.Label(ventana, text="3. De clic para pre-procesar la imagen ", bg="yellow", fg="black", font = "Arial 15")
label_3.grid (row = 7, column = 2, pady = 10)

boton_3 = tk.Button(text = "Pre-procesar", font= 'Arial 13')##, command = parametros)
boton_3.grid(row = 8, column = 2, columnspan = 2, pady = 10)

label_4 = tk.Label(ventana, text="4. Definir umbral para la masacra de agua ", bg="yellow", fg="black", font = "Arial 15")
label_4.grid (row = 9, column = 2, pady = 10)

boton_2 = tk.Button(text = "Aplicacion de mascara", font= 'Arial 13')##, command = parametros)
boton_2.grid(row = 11, column = 2, columnspan = 2, pady = 10)

cuadro_3 = tk.Entry(ventana, font = "Arial 13", justify = "left")
cuadro_3.grid (row = 10, column = 2, pady = 10)

label_5 = tk.Label(ventana, text="5. Cracion de la imagen GEOTIFF ", bg="yellow", fg="black", font = "Arial 15")
label_5.grid (row = 12, column = 2, pady = 10)

boton_2 = tk.Button(text = "Craer imagen", font= 'Arial 13')##, command = parametros)
boton_2.grid(row = 13, column = 2, columnspan = 2, pady = 10)








#textoResult = tk.Text(ventana)
#textoResult.grid(row = 12, column = 3, columnspan = 12)



















ventana.mainloop()
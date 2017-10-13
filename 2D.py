"""©Juan Diego Martínez"""
##############################

from tkinter import * #Importa todos los datos de tkinter
from tkinter import ttk #Importa la librería tkinter.ttk
from time import sleep #Importa la función sleep de la librería time
import random #Importa random
WD = Tk() #Crea ventana
WD.title("LABERINTO") #Titulo de ventana
CANVAS = Canvas(WD,width=620,height=620) #Crea canvas
ttk.Label(WD, text="LABERINTO", font=("Arial", 30, "bold")).pack() #Crea titulo
ttk.Label(WD, text="Utilice las flechas para mover la bola azul").pack() #Crea instrucción
CANVAS.pack() #Posiciona canvas
CANVAS.create_rectangle(30, 30, 590, 590, width=0) #Crea margenes
CANVAS.create_text(30,275, text="INICIO", font=("Arial", 13, "bold")) #Crea etiqueta de inicio
CANVAS.create_text(590,295, text="FIN", font=("Arial", 13, "bold")) #Crea etiqueta de final

##############################
"""FUNCIONES DE CONSTRUCCIÓN DE FIGURAS"""

def pared(x1, y1, x2, y2): #Funcion para crear paredes
    COLOR = "#%03x" % random.randint(0, 0xFFF) #Crea color aleatorio
    CANVAS.create_rectangle(x1,y1,x2,y2, fill=COLOR, width=0)

def conjunto_paredes(orientacion, iniciox, inicioy, numero, ausentes=[], longitud=80): #Funcion para construir conjunto de paredes
    if orientacion == "v":
        for CONTADOR in range(0, numero):
            if CONTADOR+1 not in ausentes:
                y = longitud * CONTADOR + inicioy
                pared(iniciox, y, iniciox+20, y+longitud)
    if orientacion == "h":
        for CONTADOR in range(0, numero):
            if CONTADOR+1 not in ausentes:
                x = longitud * CONTADOR + iniciox
                pared(x, inicioy, x+longitud, inicioy+20)

##############################
"""PAREDES AUSENTES"""
#Determina las paredes faltantes dentro del conjunto de paredes

AUSENTES_H = {1:[],
              2:[1,2,3,4,5,6,7],
              3:[1,2,4,5,6,7],
              4:[1,2,3,4,5],
              5:[2,3,7],
              6:[1,4,5,6],
              7:[1,2,7],
              8:[]}

AUSENTES_V = {1:[4],
              2:[1,5],
              3:[2,4,6,7],
              4:[1,5,6,7],
              5:[4,5,7],
              6:[1,4,7],
              7:[3,5,6,7],
              8:[4]}

##############################
"""CONSTRUCCION DE FILAS Y COLUMNAS"""

for CONTADOR in range(0, 8): #Construye paredes horizontales
    conjunto_paredes("h", 20, 20+CONTADOR*80, 7, AUSENTES_H[CONTADOR+1])

for CONTADOR in range(0, 8): #Construye paredes verticales
    conjunto_paredes("v", 20+CONTADOR*80, 20, 7, AUSENTES_V[CONTADOR+1])

#Crea paredes faltantes
pared(100, 340, 120, 360)
pared(500, 340, 520, 360)
pared(580, 260, 600, 280)
pared(580, 580, 600, 600)

##############################
"""ROBOT Y MOVIMIENTO"""

ROBOT = CANVAS.create_oval(20,290,40,310, fill="blue", width=0) #Crea bolita del robot
FIN = False

def MOVER(DIR): #Función para mover bola
    POSICION = CANVAS.coords(ROBOT)
    X1 = POSICION[0]
    Y1 = POSICION[1]
    X2 = POSICION[2]
    Y2 = POSICION[3]
    if DIR == "N":
        if len(CANVAS.find_overlapping(X1, Y1-10, X2, Y2-10)) == 2:
            CANVAS.move(ROBOT, 0, -10)
    if DIR == "S":
        if len(CANVAS.find_overlapping(X1, Y1+10, X2, Y2+10)) == 2:
            CANVAS.move(ROBOT, 0, 10)
    if DIR == "E":
        if len(CANVAS.find_overlapping(X1+10, Y1, X2+10, Y2)) == 2:
            CANVAS.move(ROBOT, 10, 0)
    if DIR == "O":
        if len(CANVAS.find_overlapping(X1-10, Y1, X2-10, Y2)) == 2:
            CANVAS.move(ROBOT, -10, 0)
    CANVAS.update_idletasks()
    if CANVAS.coords(ROBOT)[0] == 580:
        global FIN
        if FIN == False:
            VICTORIA = Toplevel(WD)
            ttk.Label(VICTORIA, text="LO LOGRASTE!", font=("Arial", 50, "bold"), foreground="blue").pack()
            FIN = True

##############################
"""COMANDOS ROBOT"""

#Asignamientos de teclas a la funcion de movimiento
WD.bind("<Up>", lambda event:MOVER("N"))
WD.bind("<Down>", lambda event:MOVER("S"))
WD.bind("<Right>", lambda event:MOVER("E"))
WD.bind("<Left>", lambda event:MOVER("O"))

##############################
"""MOVIMIENTO"""

#Espera a que la ventana esté inicializada
WD.update()
sleep(1)

def MOVER_2(DIR, NUM): #Función para mover el robot en la dirección y la cantidad de pasos dados
    for CONTADOR in range(0,NUM):
        MOVER(DIR)

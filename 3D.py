""" © Juan Diego Martínez """

from visual import *
scene.title = "Laberinto"
scene.background=color.white
scene.userzoom = False
scene.userspin = False

BOLA = sphere(pos=(-14,0,0.5), radius=0.5, color=(0,0,0.5))
box(pos=(0, 0, -0.05), size=(33,33,0.1), color=(0,0.5,0))

def BLOQUE(X, Y):
    box(pos=(X, Y, 0.5), size=(1.1,1.1,1), color=(0,1,0))

def R(I, F):
    return [X for X in range(I,F+1)]

def MOVER(XN=0, YN=0):
    X = round(BOLA.pos.x,0) + XN
    Y = round(BOLA.pos.y,0) + YN
    if X > -15 and X < 15 and Y > -15 and Y < 15:
        if X+15 not in PRESENTES[Y+15]:
            V = vector(XN, YN, 0)
            for I in range(200):
                rate(1000)
                BOLA.pos += V*0.005

PRESENTES = {1:R(1,29),
             2:[1,25,29],
             3:[1,25,29],
             4:[1,25,29],
             5:[1,25,29]+R(6,21),
             6:[1,9,13,25,29],
             7:[1,9,13,25,29],
             8:[1,9,13,25,29],
             9:[9,13,29]+R(1,5)+R(18,25),
             10:[1,9,21,29],
             11:[1,9,21,29],
             12:[1,9,21,29],
             13:[1,21]+R(5,17)+R(25,29),
             14:[5,17,25],
             15:[5,17,25],
             16:[5,17,25],
             17:[17,25]+R(1,9),
             18:[1,9,13,17,21,25,29],
             19:[1,9,13,17,21,25,29],
             20:[1,9,13,17,21,25,29],
             21:[1,9,13,25,29]+R(17,21),
             22:[1,5,9,13,17,25,29],
             23:[1,5,9,13,17,25,29],
             24:[1,5,9,13,17,25,29],
             25:[1,5,9,13,17,25,29],
             26:[1,5,13,21,29],
             27:[1,5,13,21,29],
             28:[1,5,13,21,29],
             29:R(1,29)}
             
for FILA in range(1,30):
    for COLUMNA in range(1, 30):
        if COLUMNA in PRESENTES[FILA]:
            BLOQUE(COLUMNA-15, FILA-15)

while True:
    if scene.kb.keys:
        TECLA = scene.kb.getkey()
        if TECLA == "up":
            scene.forward = (0,0.5,-1)
            MOVER(YN=1)
        if TECLA == "down":
            scene.forward = (0,-0.5,-1)
            MOVER(YN=-1)
        if TECLA == "right":
            scene.forward = (0.5,0,-1)
            MOVER(XN=1)
        if TECLA == "left":
            scene.forward = (-0.5,0,-1)
            MOVER(XN=-1)
        if round(BOLA.pos.x,0) == 14:
            text(text="Felicidades\nHas Ganado!", pos=(0,0,5), align='center', width=2, height=2, depth=-0.3, color=(0,0.2,0))
            scene.forward = (0,0,-1)
            break
    else:
        scene.forward = (0,0,-1)

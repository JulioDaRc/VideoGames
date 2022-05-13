from turtle import *

from freegames import line


def grid(): 
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)
    """Esto dibujará las líneas de nuestra cuadrícula.""" 


def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)
    """Esta función toma los parámetros x e y que dibujaran la marca de cruz para el jugador."""


def drawo(x, y):
    
    up()
    goto(x + 67, y + 15)
    down()
    circle(50)
    """Esta función yoma los parámetros x e y que dibujarán la marca O para el otro jugador."""


def floor(value):
    return ((value + 200) // 133) * 133 - 200
    """Valor redondeado a la cuadrícula con tamaño de cuadrado 133."""


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player
    """Esto verifica qué jugador debe colocar un contador (siempre comienza la cruz), dibuja la marca correcta y finalmente cambia el jugador para el siguiente turno."""


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
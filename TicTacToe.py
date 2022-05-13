from turtle import *
from state import *

def line(a, b, x, y):
    up()
    goto(a, b)
    down()
    goto(x, y)

def draw_grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)
    "Dibuja el Tablero del Gato."

def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)
    "Dibuja al jugador X"

def drawo(x, y):
    "Dibuja al jugador O"
    up()
    goto(x + 67, y + 15)
    down()
    circle(50)
    "Dibuja al jugador O"
    
def floor(value):
    return ((value + 200) // 133) * 133 - 200
    "Redondea el valor a la cuadricula con tamaño 133."

state = State()

players = [drawx, drawo]


def tap(x, y):
    x = floor(x)
    y = floor(y)
    player = state.player
    grid = state.grid;
    item = state.get_grid_item(x, y)
    "Dibuja X o O en el cuadrado respectivamente."
    
    if(grid[item[0]][item[1]] is not None):
      print("Cuadrado ya tomado")
      return
    grid[item[0]][item[1]] = player
    draw = players[player]
    draw(x, y)
    update()
    state.player = not player
  
Screen().setup(420, 420, 370, 0)
hideturtle()
Screen().tracer(0, 0)
draw_grid()
update()
Screen().onscreenclick(tap)
done()
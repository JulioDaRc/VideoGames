from turtle import *
from state import *

def line(a, b, x, y):
    up()
    goto(a, b)
    down()
    goto(x, y)

def draw_grid():
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    "Draw X player."
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    "Draw O player."
    up()
    goto(x + 67, y + 15)
    down()
    circle(50)

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

state = State()

players = [drawx, drawo]


def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state.player
    grid = state.grid;
    item = state.get_grid_item(x, y)
    
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
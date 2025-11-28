from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint
import pgzrun

TITLE="colpisci l'alieno"
WIDTH=800
HEIGHT=600

messaggio=""
alieno=Actor("alieno")

def draw():
    screen.clear()
    screen.fill(color=(69,0,0))
    alieno.draw()
    screen.draw.text(
        messaggio,
        center=(400,40),
        fontsize=60
    )
def piazza_alieno():
    alieno.x=randint(50,WIDTH -50)
    alieno.y=randint(50,HEIGHT -50)
    alieno.image="alieno"
def on_mouse_down(pos):
    global messaggio
    if alieno.collidepoint(pos):
        messaggio="bel colpo"
        alieno.image="esplosione"
    else:
        messaggio="Mancato"
piazza_alieno()
clock.schedule_interval(piazza_alieno, 1.0)
pgzrun.go()
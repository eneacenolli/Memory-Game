# implementation of card game - Memory

import simplegui
import random

lista = range(18)
exposed = []
counter = 0
turn1 = -1
turn2 = -1
state = 0
# helper function to initialize globals
def new_game():
    global lista
    global exposed
    global counter
    global turn1 , turn2 , state
    lista = range(18)
    counter = 0
    exposed = [] 
    turn1 = -1
    turn2 = -1
    state = 0
    
# define event handlers
def mouseclick(pos):
    global exposed
    global lista
    global counter
    global turn1 , turn2 ,state
    index = pos[0] / 50
    print index, exposed
    if index in exposed or index == turn1:
        return
        
    if state == 0 :
        turn1 = index
        turn2 = -1
        state = 1
    elif state == 1:
        turn2 = index
        if turn1==turn2:
            turn1=-1
            turn2=-1
            state = 0
            return
        counter += 1
        if lista[turn1]%9 == lista[turn2]%9: 
            exposed.append(turn1)
            exposed.append(turn2)
            turn1 = -1
            turn2 = -1
        state = 0 
            
# cards are logically 50x100 pixels in size    
def draw(canvas):   
    global lista
    global turns
    global counter
    if len(exposed)!=len(lista):
        label.set_text("Turns = "+str(counter))
    else:
        label.set_text("You ave finished the game in " + str(counter) + ' moves')
    for index in range(0, len(lista)):
        num = lista[index]
        value = str(lista[index] % 9)
        if num in exposed:
            canvas.draw_text(value,[10 + num * 50, 60],50,'White')
            canvas.draw_line([0 + num*50,0],[0 + num*50,100],1,'White')
        elif index == turn1 or index == turn2:
            canvas.draw_text(value,[10 + num * 50, 60],50,'White')            
        else:
            canvas.draw_polygon([[ 0 + num*50 , 0], [0 + num*50, 100], [50 + num*50, 100], [50 + num*50, 0]], 1, 'white', 'blue')
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 900, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubri
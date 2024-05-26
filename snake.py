from tkinter import *
import random
import time
WIDTH=500
HEIGHT=500
SPEED=100
PARTS=3
SIZE=25
SNAKE_COLOR="gray"
FOOD_COLOR="red"
BG_COLOR="black"
class Snake:

   def __init__(self):
       self.SIZE=PARTS
       self.coordinates=[]
       self.squares=[]
       for i in range(0,PARTS):
           self.coordinates.append([100,100])
       for x,y in self.coordinates:
           square=canvas.create_rectangle(x,y,x+SIZE,y+SIZE,
                                          fill=SNAKE_COLOR,tag="snake")
           self.squares.append(square)

class Food:
    def __init__(self):
        x=random.randint(0,(WIDTH/SIZE)-1)*SIZE
        y=random.randint(0,(HEIGHT/SIZE)-1)*SIZE
        self.coordinates=[x,y]
        canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill=FOOD_COLOR,tag="food")

def next_turn(snake,food):
    x,y=snake.coordinates[0]

    if direction=="up":
        y-=SIZE

    elif direction=="down":
        y+=SIZE

    elif direction=="left":
        x-=SIZE

    elif direction=="right":
        x+=SIZE

    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score : {}".format(score))
        canvas.delete("food")

        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)
def change_direction(new_direction):

    global direction
    if new_direction=="left":
        if direction!="right":
            direction=new_direction

    elif new_direction=="right":
        if direction!="left":
            direction=new_direction

    elif new_direction=="up":
        if direction!="down":
            direction=new_direction

    elif new_direction=="down":
        if direction!="up":
            direction=new_direction

def check_collision(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=WIDTH:
        return True
    elif y<0 or y>=HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True
    return False

def game_over():
    time.sleep(0.3)
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("Arial",50),text="Game Over!",fill="red",tag="gameover")





window =Tk()

window.title("Snake Game")
window.resizable(False,False)

score=0
direction="right"
label=Label(window,text="Score : {}".format(score),font=("Arial",30))
label.pack()

canvas=Canvas(window,bg=BG_COLOR,height=HEIGHT,width=WIDTH)
canvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event:change_direction('left'))
window.bind('<Right>', lambda event:change_direction('right'))
window.bind('<Up>', lambda event:change_direction('up'))
window.bind('<Down>', lambda event:change_direction('down'))


snake=Snake()
food=Food()

next_turn(snake,food)



window.mainloop()

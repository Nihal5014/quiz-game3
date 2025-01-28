import pgzrun
import time

WIDTH =700
HEIGHT = 600
title_box = Rect(0,0,700,95) 
question_box = Rect(14,111,520,140)
time_box = Rect(550,111,135,140)
answer_box1 = Rect(14,270,250,140)
answer_box2 = Rect(284,270,250,140)
answer_box3 = Rect(14,430,250,140)
answer_box4 = Rect(284,430,250,140)
skip_button = Rect(550,270,135,300)
answer_list = [answer_box1,answer_box2,answer_box3,answer_box4]
questions =[]
question = []
total_questions = 11
current_question = 0 
score = 0
time_left = 10
game_over= False
def draw():
    screen.fill("black")
    
    screen.draw.filled_rect(title_box,'black')
    screen.draw.filled_rect(question_box,'dark blue')
    screen.draw.filled_rect(time_box,'dark blue')
    screen.draw.filled_rect(answer_box1,'orange')
    screen.draw.filled_rect(answer_box2,'orange')
    screen.draw.filled_rect(answer_box3,'orange')
    screen.draw.filled_rect(answer_box4,'orange')
    screen.draw.filled_rect(skip_button,'green')

    screen.draw.textbox("Welcome To Quiz Master",title_box,color = "white")
    screen.draw.textbox(question[0],question_box,color = "white")
    screen.draw.textbox(str(time_left),time_box,color = "white")
    screen.draw.textbox(question[1],answer_box1,color = "white")
    screen.draw.textbox(question[2],answer_box2,color = "white")
    screen.draw.textbox(question[3],answer_box3,color = "white")
    screen.draw.textbox(question[4],answer_box4,color = "white")
    screen.draw.textbox("skip",skip_button,color = "white")

def update():
    pass

def read_file():
    global questions
    global total_questions
    file = open("questions.txt","r")
    questions = file.readlines()
    file.close()
    total_questions = len(questions)

def read_question():
    global question 
    question = questions[current_question].split(',')

def timer():
    global time_left
    global game_over
    if time_left > 0:
        time_left = time_left-1
    else:
        game_over = True 

def on_mouse_down(pos):
    option = 1
    for answer in answer_list:
        if answer.collidepoint(pos):
            if option == int(question[5]):
                correct_answer()
            else: 
                gameover()
        option = option+1

def correct_answer():
    global read_question
    global score
    global current_question
    global time_left
    time_left = 10
    score = score + 1
    current_question = current_question + 1
    if current_question >= total_questions:
        gameover()
    else:
        read_question()

def gameover():
    global message
    global question 
    global time_left
    message = "Game over! You scored"+str(score)+"marks"
    question = [message,'-','-','-','-','5']
    time_left= 0
    gameover = True 
clock.schedule_interval(timer,1)    
read_file() 
read_question()  

pgzrun.go()


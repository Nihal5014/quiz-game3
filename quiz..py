import pgzrun

WIDTH = 700
HEIGHT = 600
title_box = Rect(0, 0, 700, 95)
question_box = Rect(14, 111, 520, 140)
time_box = Rect(550, 111, 135, 140)
answer_box1 = Rect(14, 270, 250, 140)
answer_box2 = Rect(284, 270, 250, 140)
answer_box3 = Rect(14, 430, 250, 140)
answer_box4 = Rect(284, 430, 250, 140)
skip_button = Rect(550, 270, 135, 300)

answer_list = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question = ["Loading...", "-", "-", "-", "-", "5"] 
total_questions = 0
current_question = 0
score = 0
time_left = 10
game_over = False

def draw():
    screen.fill("black")
    
    screen.draw.filled_rect(title_box, 'black')
    screen.draw.filled_rect(question_box, 'dark blue')
    screen.draw.filled_rect(time_box, 'dark blue')
    screen.draw.filled_rect(answer_box1, 'orange')
    screen.draw.filled_rect(answer_box2, 'orange')
    screen.draw.filled_rect(answer_box3, 'orange')
    screen.draw.filled_rect(answer_box4, 'orange')
    screen.draw.filled_rect(skip_button, 'green')

    screen.draw.textbox("Welcome To Quiz Master", title_box, color="white")

    if not game_over:
        screen.draw.textbox(question[0], question_box, color="white")
        screen.draw.textbox(str(time_left), time_box, color="white")
        screen.draw.textbox(question[1], answer_box1, color="white")
        screen.draw.textbox(question[2], answer_box2, color="white")
        screen.draw.textbox(question[3], answer_box3, color="white")
        screen.draw.textbox(question[4], answer_box4, color="white")
        screen.draw.textbox("Skip", skip_button, color="white")
    else:
        screen.draw.textbox(f"Game Over! You scored {score} marks", question_box, color="red")

def update():
    pass

def read_file():
    global questions, total_questions
    try:
        with open("questions.txt", "r") as file:
            questions = file.readlines()
        total_questions = len(questions)
    except FileNotFoundError:
        print("Error: questions.txt not found!")
        questions.append("Error: No questions available,-,-,-,-,5")

def read_question():
    global question, current_question
    if current_question < total_questions:
        question = questions[current_question].strip().split(',')
    else:
        gameover()

def timer():
    global time_left, game_over
    if not game_over and time_left > 0:
        time_left -= 1
    elif time_left == 0:
        gameover()

def on_mouse_down(pos):
    global game_over
    if game_over:
        return
    
    option = 1
    for answer in answer_list:
        if answer.collidepoint(pos):
            if option == int(question[5]):  
                correct_answer()
            else:
                gameover()
        option += 1
    
    if skip_button.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, current_question, time_left
    score += 1
    current_question += 1
    time_left = 10
    read_question()

def skip_question():
    global current_question, time_left
    current_question += 1
    time_left = 10
    read_question()

def gameover():
    global game_over, question
    game_over = True
    question = [f"Game Over! You scored {score} marks", "-", "-", "-", "-", "5"]
    clock.unschedule(timer) 
clock.schedule_interval(timer, 1)
read_file()
read_question()

pgzrun.go()


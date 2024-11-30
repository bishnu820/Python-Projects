import turtle as t
import random as rd

# Initialize game screen
t.bgcolor('yellow')
t.title("Caterpillar Game")

# Create caterpillar
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# Create leaf
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

# Create game text and score display
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Game state variable
game_started = False


# Function to check if caterpillar is outside the window
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    x, y = caterpillar.pos()
    return x < left_wall or x > right_wall or y < bottom_wall or y > top_wall


# Function to end the game
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))


# Function to display the current score
def display_score(current_score):
    score_turtle.clear()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.penup()
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


# Function to randomly place the leaf on the screen
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-t.window_width() // 2 + 20, t.window_width() // 2 - 20))
    leaf.sety(rd.randint(-t.window_height() // 2 + 20, t.window_height() // 2 - 20))
    leaf.showturtle()


# Function to start the game
def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    # Initialize game variables
    score = 0
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    text_turtle.clear()

    # Display initial score and place the first leaf
    display_score(score)
    place_leaf()

    # Main game loop
    while True:
        caterpillar.forward(caterpillar_speed)
        # Check for collision with leaf
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 0.5  # Increment speed
            score += 10
            display_score(score)
        # Check if caterpillar goes outside the window
        if outside_window():
            game_over()
            break


# Functions to handle movement directions
def move_up():
    if caterpillar.heading() not in [90, 270]:
        caterpillar.setheading(90)


def move_down():
    if caterpillar.heading() not in [90, 270]:
        caterpillar.setheading(270)


def move_left():
    if caterpillar.heading() not in [0, 180]:
        caterpillar.setheading(180)


def move_right():
    if caterpillar.heading() not in [0, 180]:
        caterpillar.setheading(0)


# Bind keyboard inputs
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.listen()
t.mainloop()

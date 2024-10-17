import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Background color

# Create turtle object
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)  # Set speed of turtle

# Function to draw a circle
def draw_circle(radius, color, x, y):
    t.penup()
    t.goto(x, y)  # Move turtle to starting position
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a cat face
def draw_cat():
    # Draw face
    draw_circle(100, "lightgray", 0, -100)  # Cat's face

    # Draw left eye
    draw_circle(20, "white", -35, 20)  # White part
    draw_circle(10, "black", -35, 40)  # Black pupil
    
    # Draw right eye
    draw_circle(20, "white", 35, 20)  # White part
    draw_circle(10, "black", 35, 40)  # Black pupil

    # Draw nose
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw mouth
    t.penup()
    t.goto(0, 0)
    t.right(90)
    t.pendown()
    t.circle(30, 60)  # Left part of mouth
    t.penup()
    t.goto(0, 0)
    t.left(120)
    t.pendown()
    t.circle(30, 60)  # Right part of mouth

    # Draw ears
    t.penup()
    t.goto(-70, 70)
    t.pendown()
    t.color("lightgray")
    t.begin_fill()
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()

    t.penup()
    t.goto(30, 70)
    t.pendown()
    t.color("lightgray")
    t.begin_fill()
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()

# Draw the cat
draw_cat()

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()

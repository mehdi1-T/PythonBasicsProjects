import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Drawing - Radiating Lines")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
screen.tracer(1)  # Update screen every 10 lines - fast but visible
t.color("hotpink")

# Function to calculate heart border point at given angle
def heart_point(angle):
    # Parametric equations for a heart shape
    t_param = math.radians(angle)
    x = 16 * math.sin(t_param) ** 3
    y = 13 * math.cos(t_param) - 5 * math.cos(2 * t_param) - 2 * math.cos(3 * t_param) - math.cos(4 * t_param)
    return x * 15, y * 15  # Increased from 10 to 15 for bigger heart

# Start from center
center_x, center_y = 0, 0

# Draw lines from center to heart border
angle = 0
while angle < 360:
    # Get point on heart border
    border_x, border_y = heart_point(angle)
    
    # Go to center
    t.penup()
    t.goto(center_x, center_y)
    
    # Draw to border
    t.pendown()
    t.goto(border_x, border_y)
    
    # Go back to center
    t.goto(center_x, center_y)
    
    # Change angle
    angle += 2  # Change this value for more or fewer lines

# Hide turtle at the end
t.hideturtle()

# Write text below the heart
t.penup()
t.goto(0, -250)
t.color("hotpink")
t.write("I love you Hafssa", align="center", font=("Arial", 28, "bold"))

# Keep window open
turtle.done()
import turtle
import random

# Set up the turtle
turtle.setup(width=500, height=500)
turtle.speed(0)  # Set turtle speed to fastest for smoother drawing

# Define function to draw a colored circle
def draw_circle(radius, color):
  """
  Draws a circle with the given radius and color.

  Args:
    radius: The radius of the circle.
    color: The color of the circle.
  """
  turtle.penup()
  turtle.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random starting position
  turtle.pendown()
  turtle.pencolor(color)
  turtle.circle(radius)

# Draw multiple circles
for _ in range(20):  # Draw 20 circles
  radius = random.randint(10, 50)  # Random radius between 10 and 50
  color = (random.random(), random.random(), random.random())  # Random RGB color
  draw_circle(radius, color)

# Keep the window open
turtle.done()

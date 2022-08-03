from turtle import Turtle, Screen
import drawshapes


screen = Screen()
screen.bgcolor("dim gray")

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed(100)

# drawshapes.draw_shapes(timmy)
# drawshapes.random_walk(timmy)
drawshapes.draw_spirograph(timmy, 100)

screen.exitonclick()

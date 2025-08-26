import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

WALL_CORDINATE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #collsion with food
    if snake.head.distance (food) < 15:
        print("collided")
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
    #detect collision with wall
    if snake.head.xcor() > WALL_CORDINATE or snake.head.xcor() < -WALL_CORDINATE or snake.head.ycor() > WALL_CORDINATE or snake.head.ycor() < -WALL_CORDINATE:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()

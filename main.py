from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    got_out_x_axis = snake.head.xcor() > 280 or snake.head.xcor() < -280
    got_out_y_axis = snake.head.ycor() > 280 or snake.head.ycor() < -280
    the_snake_got_out_of_bounds = got_out_x_axis or got_out_y_axis

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    # Detect collission with wall
    if the_snake_got_out_of_bounds:
        scoreboard.print_game_over()
        game_is_on = False

    # Detect collission with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.print_game_over()
            game_is_on = False


screen.exitonclick()

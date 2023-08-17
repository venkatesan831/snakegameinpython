import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
sc = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True

while is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sc.scores()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        sc.reset()
        snake.reset()
        print("GAME OVER")
        is_on = False

    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            sc.reset()
            snake.reset()
            print("GAME OVER")
            is_on = False

screen.bye() 

screen.exitonclick()



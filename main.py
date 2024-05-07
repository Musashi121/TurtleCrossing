import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Fred the Crazy Turtle")
screen.tracer(0)
fred = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fred.move, "Up")

game_is_on = True
count = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if fred.ycor() > 220:
        fred.level_up()
        scoreboard.update_scoreboard()
        car_manager.cars = []

    if count == 10:
        car_manager.create_car()
        count = 0


    count += 1

screen.exitonclick()

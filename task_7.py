#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while True:
        if not wall_is_beneath():
            move_down()
        else:
            break
    
    while True:
        if not wall_is_on_the_right():
            move_right()
        else:
            break
    move_down(1)
    while True:
        if not wall_is_on_the_left():
            move_left()
        else:
            break

if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    wall_is_beneath_ = wall_is_beneath()
    while True:
        move_right(1)
        if wall_is_beneath_ and not wall_is_beneath():
            break
        else:
            wall_is_beneath_ = wall_is_beneath()

if __name__ == '__main__':
    run_tasks()

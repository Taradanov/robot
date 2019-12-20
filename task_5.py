#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    while True:
        move_right(1)
        if not wall_is_beneath():
            break



if __name__ == '__main__':
    run_tasks()

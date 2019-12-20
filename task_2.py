#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for i in range(0,3):
        move_right(1)
        move_down(1)
        if i == 1:
            fill_cell()
    else:
        move_right(1)


if __name__ == '__main__':
    run_tasks()

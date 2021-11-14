import keyboard
from time import sleep

# define wait function


def wait(seconds):
    sleep(seconds)

# define function to wait for z key


def wait_for_do_key():
    while True:
        if keyboard.is_pressed("z"):
            break
        sleep(0.01)

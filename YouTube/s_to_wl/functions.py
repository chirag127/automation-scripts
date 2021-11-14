import time
import keyboard

# define wait function
def wait(seconds):
    time.sleep(seconds)

# define function to wait for z key
def wait_for_z_key():
    while True:
        if keyboard.is_pressed("z"):
            break
        time.sleep(0.01)

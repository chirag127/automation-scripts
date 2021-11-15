import all_to_wl
from functions import *
import webbrowser

if __name__ == "__main__":

    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    while True:

        try:

            wait_for_do_key()

            all_to_wl.main()

        except Exception as e:

            print(e)

            sleep(1)

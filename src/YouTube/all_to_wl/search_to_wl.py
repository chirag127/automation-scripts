import all_to_wl
from functions import *


if __name__ == "__main__":

    while True:

        try:

            wait_for_do_key()

            all_to_wl.main()

        except Exception as e:

            print(e)

            sleep(1)

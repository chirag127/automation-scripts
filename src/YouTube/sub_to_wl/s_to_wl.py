import add100totrans
import pl_to_wl
import t_to_wl
import removewatchedvideo
from functions import *


def main():

    add100totrans.main()

    sleep(1)

    close_tab()

    sleep(0.1)

    close_tab()

    pl_to_wl.main()

    sleep(1)

    close_tab()

    t_to_wl.main()

    sleep(1)

    close_tab()

    removewatchedvideo.main()

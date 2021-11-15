from functions import *
import add100totrans
import pl_to_wl
import t_to_wl
import removewatchedvideo
import playwl


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

    # sleep(2)

    # playwl.main()


if __name__ == "__main__":

    main()

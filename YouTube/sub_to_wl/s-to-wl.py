from functions import *
import add100totrans
import pl_to_wl
import removewatchedvideo
import playwl


def main():

    add100totrans.main()

    wait(0.5)

    close_tab()

    pl_to_wl.main()

    wait(0.5)

    close_tab()

    removewatchedvideo.main()

    wait(2)

    playwl.main()


if __name__ == "__main__":

    main()

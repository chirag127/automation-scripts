# submit the issue by clicking on the submit button on the create new issue page of github and go to the next tab in the browser
# by pressing the hotkeys control+ tab

from functions import *


while True:

    wait_for_z()

    for i in range(5):

        click_submit()

        go_to_next_tab()

        wait(0.1)

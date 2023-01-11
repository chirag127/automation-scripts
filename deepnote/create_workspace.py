import names
from time import sleep
import webbrowser
import pyautogui
# Physical: {X=716,Y=612};
# Physical: {X=1019,Y=686};
# Physical: {X=668,Y=591};
# Physical: {X=614,Y=627};

def wait_sleep(time = 0.5):
    sleep(time)

def return_random_workspace_name():
    name =  names.get_full_name()
    # convert u'Patricia Halford' to 'Patricia Halford':


    return name




def open_the_create_new_workspace_url():
    url = "https://deepnote.com/workspace/ema-c1d2-d403c869-1ad9-44f8-a9de-454183a5cb92/create-new-workspace"
    webbrowser.open(url)

def choose_plan():
#     Physical: {X=716,Y=612}


    pyautogui.click(716, 612)
# Set up your Workspace
# This workspace is where your team’s projects will live. Let’s fill in some details to get started.

# Workspace name*
# asfd
# What will you be using Deepnote for?*

# Select option


def set_workspace_name(name):
    # Physical: {X=706,Y=475}

    pyautogui.click(706, 475)
    pyautogui.typewrite(name)
    wait_sleep()


def select_option():
    # Physical: {X=668,Y=591};
    pyautogui.click(668, 591)

    # Physical: {X=614,Y=627};
    pyautogui.click(614, 627)

def click_continue_on_set_up_new_workspace():
    # Physical: {X=1710,Y=662}

    pyautogui.click(1710, 662)

def click_create_workspace():
    # Physical: {X=1690,Y=737}

    pyautogui.click(1690, 737)



def main():
    open_the_create_new_workspace_url()
    wait_sleep(5)
    choose_plan()
    wait_sleep()
    set_workspace_name(return_random_workspace_name())
    wait_sleep()
    select_option()
    wait_sleep()
    click_continue_on_set_up_new_workspace()
    wait_sleep()
    click_create_workspace()
    wait_sleep()
    click_continue_on_set_up_new_workspace()
    wait_sleep()

if __name__ == "__main__":
    for i in range(5):
        main()
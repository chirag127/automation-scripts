from create_workspace import return_random_workspace_name, wait_sleep
import pyautogui

# Physical: {X=154,Y=220};
# Physical: {X=635,Y=449};
# Physical: {X=631,Y=523};
# Physical: {X=1463,Y=706};
def click_integrations():
    pyautogui.click(154, 220)

def click_drive():
    pyautogui.click(635, 449)

def click_on_text_box():
    pyautogui.click(631, 523)

def click_on_create_integrations():
    pyautogui.click(1463, 706)



def click_integration():
    click_integrations()
    wait_sleep()


    click_drive()

    wait_sleep(2)

    click_on_text_box()

    wait_sleep(0.1)

    pyautogui.typewrite("drive")

    wait_sleep()

    click_on_create_integrations()


# Physical: {X=285,Y=370};
# Physical: {X=365,Y=415};


def click_on_create_new():
    # Physical: {X=286,Y=371}

    pyautogui.click(286, 371)
    wait_sleep()

def click_on_create_new_project():
    pyautogui.click(365, 415)
    wait_sleep()

def set_project_name(name):

    pyautogui.typewrite(name)
    wait_sleep()


def create_project():

    wait_sleep()
    click_on_create_new()
    click_on_create_new_project()
    set_project_name(return_random_workspace_name())
    wait_sleep()


if __name__ == "__main__":

    wait_sleep(5)

    click_integration()
    wait_sleep()
    create_project()
    wait_sleep()
    pyautogui.hotkey('ctrl', 'tab')
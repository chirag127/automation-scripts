
prompts = """How can I save energy and reduce my monthly utility bills?
What are the benefits of mindfulness and meditation for mental health?
Can you suggest some ways to enhance my creativity and problem-solving skills?
How can I reduce my waste and live a more environmentally conscious lifestyle?
What are the benefits of volunteering and giving back to my community?
How can I improve my financial literacy and plan for my future?
Can you provide some tips for maintaining and improving my physical health and wellness?
How can I enhance my leadership skills and effectively manage a team?
What are the benefits of continuing education and professional development?
How can I reduce my technology usage and disconnect from digital devices for better mental health?
How can I reduce my carbon footprint and live a more sustainable lifestyle?
Can you suggest some healthy meal options for a vegetarian diet?
How can I manage stress and maintain work-life balance?
Can you provide some tips for effective public speaking?
What are the key elements of a successful job interview?
How can I improve my writing skills and effectively communicate my ideas?
What are the benefits of exercise and physical activity for mental and physical health?
How can I start a budget-friendly home garden and grow my own produce?
Can you provide some information about mental health resources and support?
What are the best ways to maintain and improve my personal relationships with friends and family?"""

prompts = prompts.strip().splitlines()

# import random

# random.shuffle(prompts)



import pyautogui
import pyperclip
from time import sleep

# Physical: {X=898,Y=570};
# Physical: {X=1732,Y=748};

def submit_prompt(prompt):
    pyperclip.copy(prompt)

    pyautogui.click(898, 570)

    sleep(0.1)

    pyautogui.hotkey("ctrl", "v")

    sleep(0.5)

    pyautogui.click(1732, 748)

    sleep(0.5)

    pyautogui.click(1732, 748)

    sleep(3)


    pyautogui.hotkey("ctrl", "r")

    sleep(4)


def submit_prompts(prompts):
    for prompt in prompts:
        submit_prompt(prompt)

if __name__ == "__main__":

    sleep(5)

    submit_prompts(prompts)

from time import sleep
import pyautogui
import time
import keyboard

import pyperclip


topics = """1. Is climate change real?
2. Should the death penalty be abolished?
3. Is gun control effective?
4. Is war ever justified?
5. Do video games cause violence?
6. Should tobacco products be banned?
7. Is animal testing ethical?
8. Is globalization a force for good or evil?
9. Should the rich be taxed more?
10. Should the minimum wage be raised?
11. Is universal healthcare a right?
12. Should abortion be legal?
13. Is same-sex marriage should be legal?
14. Should marijuana be legalized?
15. Is capital punishment a just punishment?
16. Should the United States have a universal basic income?
17. Should the United States abolish the Electoral College?
18. Should the United States adopt proportional representation?
19. Should the United States end its wars in the Middle East?
20. Should the United States invest more in education?
21. Should the United States invest more in infrastructure?
22. Should the United States invest more in research and development?
23. Should the United States invest more in the arts?
24. Should the United States invest more in the environment?
25. Should the United States invest more in social safety nets?
26. Should the United States invest more in the military?
27. Should the United States invest more in foreign aid?
28. Should the United States invest more in space exploration?
29. Should the United States government be more or less involved in the economy?
30. Should the United States government be more or less involved in people's lives?
31. Should the United States government be more or less involved in the world?
32. Should the United States have a two-party system?
33. Should the United States have a multiparty system?
34. Should the United States have a parliamentary system?
35. Should the United States have a presidential system?
36. Should the United States have a constitutional monarchy?
37. Should the United States have a republic?
38. Should the United States have a democracy?
39. Should the United States have a theocracy?
40. Should the United States have a secular state?
41. Should the United States be a Christian nation?
42. Should the United States be a Muslim nation?
43. Should the United States be a Jewish nation?
44. Should the United States be a Hindu nation?
45. Should the United States be a Buddhist nation?
46. Should the United States be a secular nation?
47. Should the United States be a multicultural nation?
48. Should the United States be a monolingual nation?
49. Should the United States be a multi-ethnic nation?
50. Should the United States be a single-ethnic nation?"""


topics = """1. What is your name?
2. What is your age?
3. Where are you from?
4. What do you do for a living?
5. What are your hobbies?
6. What is your favorite food?
7. What is your favorite movie?
8. What is your favorite book?
9. What is your favorite song?
10. What is your favorite color?
11. What is your favorite animal?
12. What is your favorite place to visit?
13. What is your favorite holiday?
14. What is your favorite memory?
15. What is your dream job?
16. What is your favorite thing about yourself?
17. What is your least favorite thing about yourself?
18. What is your biggest fear?
19. What is your biggest goal?
20. What is your favorite thing to do when you are bored?
21. What is your favorite thing to do when you are stressed?
22. What is your favorite thing to do when you are happy?
23. What is your favorite thing to do when you are sad?
24. What is your favorite thing to do when you are angry?
25. What is your favorite thing to do when you are in love?
26. What is your favorite thing to do when you are with friends?
27. What is your favorite thing to do when you are with family?
28. What is your favorite thing to do when you are alone?
29. What is your favorite thing to do when you are at home?
30. What is your favorite thing to do when you are on vacation?
31. What is your favorite thing to do when you are traveling?
32. What is your favorite thing to do when you are exploring?
33. What is your favorite thing to do when you are learning?
34. What is your favorite thing to do when you are creating?
35. What is your favorite thing to do when you are helping others?
36. What is your favorite thing to do when you are making a difference?
37. What is your favorite thing to do when you are living life to the fullest?
38. What is your favorite thing to do when you are happy and healthy?
39. What is your favorite thing to do when you are surrounded by loved ones?
40. What is your favorite thing to do when you are living your best life?"""


topics = """What is the mathematical proof of the Riemann Hypothesis?
Can you provide a solution to the Navier-Stokes equations in three dimensions?
What is the ultimate fate of the universe?
What is the meaning of life?
Can we ever achieve true artificial intelligence?
What is the nature of consciousness?
Can we travel faster than the speed of light?
How can we reconcile quantum mechanics and general relativity?
What is the origin of the universe?
What is the most efficient algorithm for sorting a large dataset?
How can we solve the P versus NP problem?
Can we prove the existence of God?
Can we create a perpetual motion machine?
How can we cure cancer?
Can we unify all the fundamental forces of nature?
What is the true nature of dark matter?
How can we build a self-sustaining colony on Mars?
Can we create a human brain in a laboratory?
How do we solve the problem of world hunger?
What is the most effective way to combat climate change?
Can we create a vaccine for HIV?
How do we achieve world peace?
Can we achieve immortality?
What is the most efficient way to store and retrieve information?
Can we create life from scratch?
How do we prevent a global pandemic?
Can we create a computer that is more powerful than the human brain?
What is the optimal way to allocate resources in a society?
Can we create a true artificial ecosystem?
How do we ensure the ethical use of technology?
What is the best way to educate children?
How do we achieve gender equality?
Can we create a sustainable energy source that can replace fossil fuels?
How do we combat income inequality?
Can we create a truly democratic society?
What is the best way to govern a society?
How do we prevent the abuse of power?
Can we create a way to communicate with extraterrestrial life forms?
How do we prevent the spread of misinformation?
Can we achieve true social justice?
How do we prevent the destruction of natural habitats?
Can we create a method for predicting earthquakes and other natural disasters?
How do we solve the problem of antibiotic resistance?
What is the most effective way to combat poverty?
Can we create a way to manipulate gravity?
How do we ensure the preservation of human rights?
Can we create a way to transfer human consciousness to a machine?
How do we prevent the spread of nuclear weapons?
Can we create a way to terraform other planets?
How do we ensure the survival of the human race in the long-term future?"""




topics = """What is the difference between a variable and a constant in programming?
What is a data structure?
What is object-oriented programming?
What is a class in programming?
What is inheritance in programming?
What is polymorphism in programming?
What is encapsulation in programming?
What is abstraction in programming?
What is a conditional statement in programming?
What is a loop in programming?
What is recursion in programming?
What is a function in programming?
What is a parameter in programming?
What is a return value in programming?
What is an array in programming?
What is a linked list in programming?
What is a tree in programming?
What is a stack in programming?
What is a queue in programming?
What is a hash table in programming?
What is a sorting algorithm in programming?
What is a searching algorithm in programming?
What is a binary search tree in programming?
What is a graph in programming?
What is a database in programming?
What is SQL?
What is a primary key in SQL?
What is a foreign key in SQL?
What is a join in SQL?
What is a subquery in SQL?
What is a trigger in SQL?
What is a stored procedure in SQL?
What is a cursor in SQL?
What is a transaction in SQL?
What is a view in SQL?
What is a constraint in SQL?
What is a web application?
What is HTML?
What is CSS?
What is JavaScript?
What is AJAX?
What is a server-side scripting language?
What is PHP?
What is Ruby on Rails?
What is Flask?
What is Django?
What is a RESTful API?
What is OAuth?
What is JWT?
What is a microservice architecture?"""








# split the topics into a list of topics to be used in the prompt by line seperating them
topics = topics.splitlines()


def main():
    # Physical: {X=868,Y=971}

    sleep(2)
    pyautogui.click(868, 971)
    for topic in topics:
        prompt = f"@Bard#9070 {topic}."

        # copy the prompt
        pyperclip.copy(prompt)

        sleep(0.1)

        pyautogui.hotkey("ctrl", "v")

        sleep(0.1)

        # press enter to submit the prompt
        pyautogui.press("enter")
        sleep(2)


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("ctrl+v"):
            main()
        else:
            time.sleep(0.1)

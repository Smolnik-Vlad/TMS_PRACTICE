from typing import List
import random
class Mystery:
    def __init__(self, question: str, answer: str, choices: List):
        self.__question = question
        self.__answer = answer
        self.__choices = choices

        self.__mix_questions=choices.copy()
        self.__mix_questions.append(self.__answer)
        random.shuffle(self.__mix_questions)
        self.__enum_list=dict(enumerate(self.__mix_questions))

    def quiz(self):
        print(f"Question: {self.__question}")
        for key, value in self.__enum_list.items():
            print(f"{key}: {value}")
        select_option: int = int(input("Select option: "))

        print(True if self.__enum_list[select_option] == self.__answer else False)


a=Mystery(question="Откуда на Беларусь готовилось нападение?",
             answer="там 4 позиции, я карту принёс, сейчас покажу",
             choices=[
                "Откуда мне знать?",
                "Со склада грязи.",
                "С планеты Нибиру.",
                "С загнивающег запада."
                ])
a.quiz()



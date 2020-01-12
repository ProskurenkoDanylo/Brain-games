import random


MAIN_QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def generating_a_question_and_answer():
    num = random.randint(1, 100)
    question = "Question: {}".format(num)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return question, correct_answer

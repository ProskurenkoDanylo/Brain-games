from random import randint, choice

MAIN_QUESTION = "Find the greatest common divisor of given numbers."


def gcd_calculating(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2


def generating_a_question_and_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = None
    question = ("Question: {} {}\n".format(number1, number2))
    correct_answer = gcd_calculating(number1, number2)
    return question, correct_answer

from operator import add, sub, mul
from random import choice, randint

MAIN_QUESTION = "What is the result of the expression?"

OPERATIONS = (
    ("+", add),
    ("-", sub),
    ("*", mul)
)


def generating_a_question_and_answer():
    operator, operation = choice(OPERATIONS)
    number2 = randint(1, 100)
    number1 = randint(1, 100)
    question = ("Question: {} {} {}\n".format(number1, operator, number2))
    correct_answer = str(operation(number1, number2))
    return question, correct_answer

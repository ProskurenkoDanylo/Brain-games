from random import choice, randint

main_question = "What is the result of the expression?"


def generating_a_question_and_answer():
    operator = choice(['*', '-', '+'])
    number2 = randint(1, 100)
    number1 = randint(1, 100)
    question = ("{} {} {}\n".format(number1, operator, number2))
    correct_answer = None
    if operator == '*':
        correct_answer = number1 * number2
    elif operator == '-':
        correct_answer = number1 - number2
    elif operator == '+':
        correct_answer = number1 + number2
    return question, correct_answer

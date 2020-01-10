from random import randint, choice
import math

main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = math.sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def generating_a_question_and_answer():
    number = randint(1, 1000)
    question = "{}\n".format(number)
    correct_answer = ''
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer

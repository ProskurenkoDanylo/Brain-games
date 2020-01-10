from random import randint, choice

main_question = 'What number is missing in the progression?'


def generating_a_question_and_answer():
    j = 1
    d = randint(1, 10)
    number1 = randint(1, 30)
    progression = [number1]
    correct_answer = None
    while j < 10:
        progression.append(progression[j - 1] + d)
        j = j + 1
    index = randint(0, 9)
    correct_answer = progression[index]
    progression[index] = ".."
    question = ("{}\n".format(' '.join(map(str, progression))))
    return question, correct_answer

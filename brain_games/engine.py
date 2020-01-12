import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    print(game.MAIN_QUESTION)
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    rounds = 3
    while rounds:
        question, correct_answer = game.generating_a_question_and_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            rounds -= 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}."
                  .format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            rounds = 0
            return None

    print('Congratulations, {}!'.format(name))

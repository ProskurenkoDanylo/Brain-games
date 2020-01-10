from brain_games.cli import on_wrong_answer
import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    print(game.main_question)
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    rounds = 3
    while rounds:
        question, correct_answer = game.generate_question()
        answer = prompt.string('{} '.format(question))
        if answer == correct_answer:
            print("Correct!")
            rounds -= 1
        else:
            return on_wrong_answer(answer, correct_answer, name)

    print('Congratulations, {}!'.format(name))

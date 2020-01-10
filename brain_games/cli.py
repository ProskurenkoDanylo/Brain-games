def on_wrong_answer(answer, correct_answer, name):
    print("{} is wrong answer ;(. Correct answer was {}."
          .format(answer, correct_answer))
    print("Let's try again, {}!".format(name))

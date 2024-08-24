from utils.input_validator import input_validator
from game_logic.hint_generator import provide_hint
from game_logic.number_generator import generate_random_number
import numpy as np

def main():
    score = 100
    actual_number = generate_random_number(1,100)
    print(actual_number)
    while True :
        user_input = input_validator(1, 100)
        if user_input == actual_number:
            print('your guess is correct')
            print(f'your score is {score}')
            break
        else: 
            hint = provide_hint(user_input, actual_number)
            score -= 10
            score = max(0,score)
            print(f'your score is {score}')


        


if __name__ == '__main__':
    main()



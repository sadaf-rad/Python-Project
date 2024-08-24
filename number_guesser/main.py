import random 
def validate_input(user_guess):
    if not user_guess.isdigit():
        print ("enter a number ")
        return False
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1 :
        print(" your guess is out of range ")
        return False
    return True
rand_num = random.randint(1,100)   
print(rand_num)
def start_game ():
    rand_num = random.randint(1,100)
    score = 100

    while True :
        user_guess = input ("guess a number between 1 and 100:")
        if user_guess == 'q':
            print('Goodbye!')
            break

        if not validate_input(user_guess):
            continue
        user_guess = int(user_guess)



        if user_guess < rand_num :
            print("guess a number bigger ")
        elif user_guess> rand_num:
            print("guess a smaller  number")
        else :
            print ("congrats you won")
        score -= 10
        score = max(score,0)
        print(score)

if __name__ == '__main__':
    start_game()


import random 


class RPS :
    def __init__(self,name) :
        self.choices = ['rock','paper','scissors']
        self.player_name = name

    def get_player_choice (self):
        user_choice = input(f'Enter your choice({self.choices}):')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
            
        else:
            print(f"Invalid choice, You havebto select from({self.choices}).")
            return self.get_player_choice()
        
    def get_computer_choice (self):
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice , computer_choice):
        if user_choice == computer_choice :
            print ('its a tie!')
        win_combinantion= [('rock','scissors'),('paper', 'rock'), ('scissor','rock')]
        for win_com in win_combinantion:
            if (user_choice == win_com[0]) & (computer_choice == win_com[1]):
                return "congrats , you won! "
        return 'oh, NO , The computer won!'

    def play (self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f'computer choice = ({computer_choice})')
        print(winner_msg)


game = RPS("sadaf")

if __name__ == '__main__': 
    while True:
        game.play()

        continue_game = input('Do you want to play another round? (Enter any key to play again! , enter q,Q to exit !)')
        if continue_game.lower() == 'q' :
            break

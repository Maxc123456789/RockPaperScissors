import random

print(' Welcome to Rock, Paper, Scissors')
def rock_paper_scissors( score_user=0, score_comp=0):
    user_choice = input(" chose your choice betwenn Rock, paper, Scissors: ").lower()
    computer_choice = random.choice(['rock','paper','scissors'])
    if user_choice not in ['rock','paper','scissors']:
        rock_paper_scissors(score_user, score_comp)
    if user_choice == computer_choice:
        print(f'its a tie  you chose {user_choice} and computer chose {computer_choice} nobody won')
    elif user_choice == "rock" and computer_choice == 'scissors' or\
        user_choice == 'scissors' and computer_choice =='paper' or\
        user_choice == 'paper' and computer_choice == 'rock' :
        print( 'you won')
        score_user +=1
    else:
        print('computer wins! so you lost ')
        score_comp +=1

    print(f' score - you {score_user}\n'
          f'score - comp {score_comp}')

    play_again = input('Do you want to play again: yes or No \n')
    if play_again == 'yes' :
        rock_paper_scissors(score_user, score_comp)
    else:
        print('Thanks for playing ')


rock_paper_scissors()
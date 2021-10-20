player_move = ''
computer_move = ''


def starter_menu():
    print("""
           ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

    
""")
    print("welcome to Rock Paper Scissor developed by HASHAR MUJAHID")
    print('please enter your move \n R : rock \n P : paper \n S : scissor')
    selection = input("enter the letters for the move selection : ")
    global player_move
    player_move =selection



def computer():
    import random
    list_choices = ['R', 'P', 'S']
    computer_choice = random.choice(list_choices)
    global computer_move
    computer_move=computer_choice


def winner_selection():
    starter_menu()
    computer()
    if player_move == 'R' and computer_move== 'P':
        print("""" 
        your move was Rock 
        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
        and computer move was Paper
        
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        so AI wins
        """)
    if player_move == 'P' and computer_move== 'S':
        print("""
        your move was Paper
        
        
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)  
        
        and computer move was sicssor
        
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        so AI wins
        
        """)
    if player_move == 'R' and computer_move== 'S':
        print("""" 
        your move was Rock 
        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        and computer move was sicssor
        
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    
    so you wins

        """)

    if player_move == 'S' and computer_move== 'R':
        print("""" 
        your move was Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        

        and computer move was ROCK
        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
    so AI wins

        """)
    if player_move == 'S' and computer_move== 'P':
        print("""
        your move was  Scissor
        
        
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        
        and computer move was Paper
        
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)  
        so You wins
        
        """)

    if player_move == 'P' and computer_move== 'R':
        print("""" 
        your move was Paper
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        
        and computer move was Rock
        
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
        so You wins
        """)

    if player_move == computer_move:
        print(
            'Tied '
        )

winner_selection()

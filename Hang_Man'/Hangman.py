import random

print("WELCOME TO HANGMAN DEVELOPED BY HASHAR MUJAHID")
WORDS = ["python", "jumble", "easy",  "answer"]
ran_word = random.choice(WORDS)
print(ran_word)
line = []
for j in range(0, len(ran_word), 1):
    line.append("_")
print(line)
HANGMANPICS = [ '''
  +---+
  |   |
  O   |
      |
      | 
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
guess_count =0
while guess_count<=len(HANGMANPICS)-1:
    guess = str(input('enter your guess'))
    for i in range(len(ran_word)):
        if ran_word[i] == guess:
            line.pop(i)
            line.insert(i, guess)
            print(line)
    else:
        if guess not  in ran_word:
            print(HANGMANPICS[guess_count])
            guess_count+=1
    if line.count('_')==0:
        print('you won')
else:
    print("you lost")

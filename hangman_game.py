from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
  graphic = [
  """ 
        +------+
        |
        |
        |
        |
        |
      =============
  """,
  """
        +------+
        |      |
        |      O
        |
        |
        |
      =============
  """,
  """
        +------+
        |      |
        |      O
        |      |
        |
        |
      =============
  """,
  """
        +------+
        |      |
        |      O
        |     -| 
        |
        |
      =============
   """,
   """
        +------+
        |      |
        |      O
        |     -|-
        |
        |
      =============
  """,
  """
        +------+
        |      |
        |      O
        |     -|- 
        |     /
        |
      =============
  """,
  """
        +------+
        |      |
        |      O
        |     -|- 
        |     / \
        |
      =============
  """]

  print graphic[hangman]
  return

def start():
  print "Let's play the Hangman game."
  while game():
    pass
  scores()

def game():
  dictionary = ["zebra","elephant","dog","monkey","rabbit","tiger"]
  word = choice(dictionary)
  word_len = len(word)
  clue = word_len*["_"]
  tries = 6
  letters_tried = ""
  guesses = 0
  letters_right = 0
  letters_wrong = 0
  global computer_score, player_score

  while(letters_wrong != tries) and ("".join(clue)!= word):
    letter=guess_letter()
    if len(letter)==1 and letter.isalpha():
      if letters_tried.find(letter) != -1:
        print "You have already picked", letter
      else:
        letters_tried = letters_tried+ letter
        first_index = word.find(letter)
        if first_index==-1:
          letters_wrong+=1
          print "Sorry",letter,"is wrong one."
        else:
          letters_right+=1
          print "Congratulations", letter, "is correct."
          for i in range(word_len):
            if letter == word[i]:
              clue[i] = letter
    else:
      print "Choose another."

    hangedman(letters_wrong)
    print " ".join(clue)
    print "Guesses: ", letters_tried

    if letters_wrong == tries:
      print "Game Over."
      print "The word was", word
      computer_score+=1
      break
    if "".join(clue) == word:
      print "You Win!"
      print "The word was",word
      player_score +=1
      break
  return play_again()

def guess_letter():
  print
  letter =  raw_input("Take a guess at our mystery word which is the name of animal:")
  letter.strip()
  letter.lower()
  print
  return letter

def play_again():
  answer = raw_input("Would you like to play again? y/n: ")
  if answer in("Y", "y", "yes", "Yes", "of course"):
    return answer
  else:
    print "Thankyou for palying game"

def scores():
  global palyer_score, computer_score
  print "High Scores"
  print "Player", player_score
  print "Computer", computer_score

if __name__ == '__main__':
  start()
         
         
         
         

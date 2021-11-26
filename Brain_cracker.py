# define a varaible and assing a dictionary data to it
# Requires user to select common noun
# the computer pick a random number as an index
# All the players of the game guess the noun
# if anyone gets it the loop will break and congartulate the player
# else the loops: 
# After all players the program runs again
from random import shuffle 
from random import randint
from typing import Counter

class word_guess(object):
    def __init__(self, numOfPlayer):
        #super(word_guess, self).__init__(*args))
        self.numOfPlayer= numOfPlayer
    #def hasWin(hasWin):
        self.WordToGuess={"Fruit":["Bananas","Orange","papaya","Mango","watermelon","Coffee","apples","Pineapple","grapes","coconut","fig"],
         "West-African":["Nigeria","Ghana","Guinea","Cameroon","Niger","Cote d'Ivoire","Mauritania","Mali","Burkina Faso","Senegal","Benin","togo"],
         "Metals":["Gold","sliver","calcium","Zinc","Aluminum","Bronz","copper"], "colour":["red","Blue","pink","Orange","Volent","Gray","white","Black","yellow"]
        }
        self.hintDiscription={"Fruit":"Hint: Its a type of Fruit ", "West-African":"Hint: Its a Country in West Africa","Metal":"Its a type of metal"
                                ,"colour":"Hint: Its a type of Colour "      }
          
        self.shufword=list(self.WordToGuess)
        

play=word_guess(4)

shuffle(play.shufword)
wordBank=play.shufword
#print(play.shufword)
def playGam(wordBank):
    guessWord=""
    hintOfWord=""
    for item in wordBank:
        #print(play.WordToGuess[item])
        hintOfWord=item
        ranNum=len(play.WordToGuess[item]) -1
        selectNum= randint(0, ranNum)
        guessWord= play.WordToGuess[item][selectNum]
        break
    arryWordBank=list(guessWord)
    lenOfWordArr=len(arryWordBank)-2
    print(arryWordBank[0],"__  "*lenOfWordArr,arryWordBank[-1])
    print(play.hintDiscription[hintOfWord])
    Counter=1
    while(play.numOfPlayer>Counter):
         #print(guessWord, play.hintDiscription[hintOfWord], arryWordBank) # uncommect to hack the game
         print("Player",Counter)
         inputGuess= input("Write in the full spelling of the guess word: ")
         print(guessWord.capitalize())
         if inputGuess==guessWord or inputGuess== guessWord.capitalize() or inputGuess==guessWord.upper():
              print("Congratulation!!! you win ")
              break
         else:
               print("Sorry,Your are Wrong")
         Counter +=1
         if Counter==play.numOfPlayer:
             break
    #playGam(wordBank)         
playGam(wordBank)

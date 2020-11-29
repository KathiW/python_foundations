"""

# Lab: Virtuous Dice

## Summary

Simulate a one person game played with a pair of 6-sided dice.                
              
Rules:

* __First roll__ 
  - 7 or 11 results in a win.
  - 2, 3, or 12 results in a loss.
  - All other values roll again.
* __Subsequent rolls__
  - A total matching the first roll results in a win.
  - 7 results in a loss.
  - All other values roll again.

## Requirements: 
* Faithfully simulate the game
* Output results to the console
* No money changes hands
    
## Stretch Goals
* Allow multiple players to play in succession.
* Validate arguments and throw appropriate exceptions.
* Write unit tests.
* Build a graphical interface.

## Hints 
* Lorem 
* Ipsum
* Sic

"""

import random
from enum import Enum

class Die:
  def __init__(self,sideCount=6):
    self.sideCount = sideCount
    self.value=None
  
  def roll(self):
    self.value = random.randrange(1,self.sideCount+1)
  

class Cup:
  def __init__(self,dice):
    self.dice = dice

  def roll(self):
    pass #TODO: .dice.forEach(d=>d.roll());
  
  def value(self):
    sum = 0
    for die in self.dice:
      sum += die.value
    return sum



class Outcome(Enum):
  Undecided=0
  Win=1
  Loss=-2





class Game:
  def __init__(self,playerName):
    self.playerName=playerName
    self.outcome = Outcome.Undecided
    self.cup= Cup([Die(), Die()])
  

  def shoot(self):
    self.cup.roll()
    #console.log(`${this.playerName} rolls a ${this.cup.value}`);
    return self.cup.value
  

#   _won(){
#     this.outcome= Outcome.Win;
#     console.log('Game Over: Won!');
#     this._over();
#   }

#   _lost(){
#     this.outcome= Outcome.Loss;
#     console.log('Game Over: Lost');
#     this._over();
#   }

  def play(self):
    firstRoll = self.shoot()

    if firstRoll in [2,3,12]:
      raise AssertionError("you lost")

    if firstRoll in [7,11]:
      raise AssertionError("you won!")
    
    while(self.outcome == Outcome.Undecided):
      result = self.shoot()

      if result==7:
        raise AssertionError("you lost")

      if result==firstRoll:
        raise AssertionError("you won!")
        






class Table:
  def __init__(self,players):
    self.players = players
    self.gameNumber=0  

  def getCurrentPlayer(self):
    return self.players[self.gameNumber%self.players.length]
  

  def playGame(self):
    self.gameNumber += 1
    game = Game(self.currentPlayer)
    game.play();
    console.log();
  






def main():
  d0 = Die()
  d0.roll()
  print(d0.value)

if __name__ == "__main__":
    main()











# const table = new Table(["Dave", "Erin", "Heather","Varoon"]);

# table.playGame();

# console.log();
# console.log('Lab complete!');
# console.log();
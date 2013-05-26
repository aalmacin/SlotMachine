# Source File Name: slotmachine.py
# Author's Name: Aldrin Jerome Almacin
# Last Modified By: Aldrin Jerome Almacin
# Date Last Modified: Saturday May 25, 2013
"""
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module
"""

# import statements
import random
from Tkinter import *

def main():
  slot_machine = SlotMachine(500, 1000)
  slot_machine.start_game()

class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
    self.POSSIBLE_BETS = "10, 20, 50, 100"
    self.symbols = []
    self.__create_symbols()
    self.JACKPOT_INCREASE_RATE = .15

    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash

    self.set_initial_values()

  def set_initial_values(self):
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*[""]
    self.turns = 0
    self.bet = 10
    self.wins = 0
    self.loses = 0

  def __create_symbols(self):
    self.symbols.append(Symbol("Blank", 0, 0, 2))
    self.symbols.append(Symbol("Grapes", 20, 2))
    self.symbols.append(Symbol("Banana", 30, 2))
    self.symbols.append(Symbol("Orange", 40, 3))
    self.symbols.append(Symbol("Cherry", 100, 4))
    self.symbols.append(Symbol("Bar", 200, 5))
    self.symbols.append(Symbol("Bell", 300, 10))
    self.symbols.append(Symbol("Seven", 1000, 20, 10))

  def start_game(self):
    # Start the game Loop
    continue_playing = True
    while (continue_playing):
      print("This is Aldrin's Slot Machine")
      print("What do you want to do?")
      print("1: Set Bet")
      print("2: Spin")
      print("3: Reset")
      print("4: Quit")
      selection = raw_input(">>> ")

      if (selection == "1"):
        self.set_bet()
      elif (selection == "2"):
        self.spin()
      elif (selection == "3"):
        self.reset()
      elif (selection == "4"):
        continue_playing = False
      else:
        print("Invalid Value entered")

  def set_bet(self):
    bet_selected = -1
    while True:
      print("How much would you bet?")
      print self.POSSIBLE_BETS
      bet_selected = raw_input(">>> ")
      if (bet_selected in self.POSSIBLE_BETS.split(", ")):
        break
      else:
        print("Invalid bet value!")
    self.bet = int(bet_selected)

  def spin(self):
    self.__pay()
    self.__increase_jackpot()

    for spin in range(3):
      spinned_result = random.randint(0, 100)

      if spinned_result in range(0, 40):
          self.results[spin] = self.symbols[0].name
      elif spinned_result in range(40, 56):
          self.results[spin] = self.symbols[1].name
      elif spinned_result in range(56, 70):
          self.results[spin] = self.symbols[2].name
      elif spinned_result in range(70, 82):
          self.results[spin] = self.symbols[3].name
      elif spinned_result in range(82, 89):
          self.results[spin] = self.symbols[4].name
      elif spinned_result in range(89, 95):
          self.results[spin] = self.symbols[5].name
      elif spinned_result in range(95, 99):
          self.results[spin] = self.symbols[6].name
      elif spinned_result in range(99, 100):
          self.results[spin] = self.symbols[7].name

    self.__check_results()

  def __pay(self):
    print("Cash Before: ", self.current_cash)
    self.current_cash -= self.bet
    print("Cash after Payed: ", self.current_cash)

  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * self.JACKPOT_INCREASE_RATE))

  def __check_results(self):
    win = False
    for symbol in self.symbols:
      if self.results.count(symbol.name) == 3:
        self.current_cash += self.bet * symbol.win_rate_full
        win = True
      if self.results.count(symbol.name) == 2:
        self.current_cash += self.bet * symbol.win_rate_two
        win = True
    if self.results.count(self.symbols[0].name) == 0 and not win:
      self.current_cash += self.bet * self.symbols[0].bonus_win_rate
    if self.results.count(self.symbols[7].name) == 1 and not win:
      self.current_cash += self.bet * self.symbols[7].bonus_win_rate

    print self.results
    print "Cash",
    print self.current_cash
    print "Bet",
    print self.bet

  def reset(self):
    self.set_initial_values()

class Symbol:
  def __init__(self, name, win_rate_full, win_rate_two, bonus_win_rate = 0):
    self.name = name
    self.win_rate_full = win_rate_full
    self.win_rate_two = win_rate_two
    self.bonus_win_rate = bonus_win_rate

  def get_win_rate_full():
    return self.win_rate_full

  def get_win_rate_two():
    return self.win_rate_two

  def get_bonus_win_rate():
    return self.bonus_win_rate

  def get_name():
    return self.name

if __name__ == "__main__": main()

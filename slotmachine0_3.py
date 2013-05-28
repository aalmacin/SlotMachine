# Source File Name: slotmachine0_2.py
# Author's Name: Aldrin Jerome Almacin
# Last Modified By: Aldrin Jerome Almacin
# Date Last Modified:
"""
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module
  Version: 0.2: Slot machine console game
"""

# import statements
import random
import pygame

pygame.init()
FRAME_RATE = 30
GAME_TITLE = "Slot Machine"
BACKGROUND_IMAGE_NAME = "images/background.png"

class SlotMachineButton(pygame.sprite.Sprite):
  def __init__(self, image_name, value, pos):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image_name)
    self.image = self.image.convert()
    self.rect = self.image.get_rect()
    self.value = value
    self.rect = self.rect.move(pos)
    self.pos = pos

  def get_value(self):
    return self.value

class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
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

  def set_bet(self, bet):
    self.bet = bet

  def get_bet(self):
    return self.bet

  def spin(self):
    self.__pay()
    self.__increase_jackpot()

    for spin in range(3):
      spinned_result = random.randint(0, 100)

      if spinned_result in range(0, 40):
          self.results[spin] = self.icons[0].name
      elif spinned_result in range(40, 56):
          self.results[spin] = self.icons[1].name
      elif spinned_result in range(56, 70):
          self.results[spin] = self.icons[2].name
      elif spinned_result in range(70, 82):
          self.results[spin] = self.icons[3].name
      elif spinned_result in range(82, 89):
          self.results[spin] = self.icons[4].name
      elif spinned_result in range(89, 95):
          self.results[spin] = self.icons[5].name
      elif spinned_result in range(95, 99):
          self.results[spin] = self.icons[6].name
      elif spinned_result in range(99, 100):
          self.results[spin] = self.icons[7].name

    self.__check_results()

  def __pay(self):
    self.current_cash -= self.bet

  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * self.JACKPOT_INCREASE_RATE))

  def __check_results(self):
    win = False
    for icon in self.icons:
      if self.results.count(icon.name) == 3:
        self.current_cash += self.bet * icon.win_rate_full
        win = True
      if self.results.count(icon.name) == 2:
        self.current_cash += self.bet * icon.win_rate_two
        win = True
    if self.results.count(self.icons[0].name) == 0 and not win:
      self.current_cash += self.bet * self.icons[0].bonus_win_rate
    if self.results.count(self.icons[7].name) == 1 and not win:
      self.current_cash += self.bet * self.icons[7].bonus_win_rate

    #TODO Jackpot

    print self.results
    print "Cash",
    print self.current_cash
    print "Bet",
    print self.bet

  def reset(self):
    self.set_initial_values()

def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  slot_machine = SlotMachine(500, 1000)

  BUTTON_BOTTOM_POS = background.get_height() - 150

  distance_between_buttons = 30
  x = 30
  bet_buttons_hash = [{"image_name": "ten_button.png", "value": 10}, {"image_name": "twenty_button.png", "value": 20}, {"image_name": "fifty_button.png", "value": 50}, {"image_name": "hundred_button.png", "value": 100}]
  bet_buttons = pygame.sprite.Group()

  for bet_button in bet_buttons_hash:
    slot_machine_btn = SlotMachineButton("images/" + bet_button["image_name"], bet_button["value"], (x, BUTTON_BOTTOM_POS))
    bet_buttons.add(slot_machine_btn)
    x += slot_machine_btn.image.get_width() + distance_between_buttons

  clock = pygame.time.Clock()

  continue_playing = True
  while (continue_playing):
    # Tick
    clock.tick(FRAME_RATE)

    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        continue_playing = False
      elif (event.type == pygame.MOUSEBUTTONDOWN):
        for bet_button in bet_buttons:
          if(bet_button.rect.collidepoint(event.pos)):
            slot_machine.set_bet(bet_button.get_value())

    screen.blit(background, background.get_rect())

    # Update to make sure that the rect follows the image
    bet_buttons.update()
    for bet_button in bet_buttons:
      screen.blit(bet_button.image, bet_button.pos)

    pygame.display.flip()

def main():
  start_game()

if __name__ == "__main__": main()

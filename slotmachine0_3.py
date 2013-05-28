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
import time

pygame.init()
FRAME_RATE = 30
GAME_TITLE = "Slot Machine"
BACKGROUND_IMAGE_NAME = "images/background.png"

"""
  Class: SlotMachineButton
"""
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

"""
  Class: SlotMachineActionButton
"""
class SlotMachineActionButton(pygame.sprite.Sprite):
  def __init__(self, image_name, method_to_be_called, pos):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image_name)
    self.image = self.image.convert()
    self.rect = self.image.get_rect()
    self.rect = self.rect.move(pos)
    self.method_to_be_called = method_to_be_called
    self.pos = pos

  def call_method(self):
    self.method_to_be_called()

  def get_pos(self):
    return self.pos

"""
  Class: SlotMachine
"""
class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
    self.JACKPOT_INCREASE_RATE = .15

    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash
    self.icons = []
    self.__create_icons()
    self.set_initial_values()

  def set_initial_values(self):
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*["Siete"]
    self.turns = 0
    self.bet = 10
    self.wins = 0
    self.loses = 0

  def __create_icons(self):
    self.icons.append(Icon("Sad Face", 0, 0, "sadface.png", bonus_win_rate = 2))
    self.icons.append(Icon("Katipunero Hat", 20, 2, "katipunero_hat.png"))
    self.icons.append(Icon("Bandana", 30, 2, "bandana.png"))
    self.icons.append(Icon("Camesa De Chino", 40, 3, "camesa_de_chino.png"))
    self.icons.append(Icon("Banyal", 100, 4, "banyal.png"))
    self.icons.append(Icon("Tsinelas", 200, 5, "tsinelas.png"))
    self.icons.append(Icon("Arnis", 300, 10, "arnis.png"))
    self.icons.append(Icon("Siete", 1000, 20, "siete.png", bonus_win_rate = 10))

  def set_bet(self, bet):
    self.bet = bet

  def get_bet(self):
    return self.bet

  def get_current_cash(self):
    return self.current_cash

  def get_current_jackpot(self):
    return self.current_jackpot

  def get_icons(self):
    return self.icons

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
    time.sleep(3)

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

  def get_results(self):
    return self.results

  def reset(self):
    self.set_initial_values()

"""
  Class: Icon
"""
class Icon(pygame.sprite.Sprite):
  def __init__(self, name, win_rate_full, win_rate_two, icon_image, bonus_win_rate = 0):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.image = pygame.image.load("images/" + icon_image)
    self.image = self.image.convert()
    self.rect = self.image.get_rect()
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

  def get_image():
    return self.image

"""
  Class: DigitalFont
"""
class DigitalFont(pygame.sprite.Sprite):
  def __init__(self, text, method, pos):
    pygame.sprite.Sprite.__init__(self)
    self.digital_font = pygame.font.Font("fonts/DS-DIGIT.TTF", 32)
    self.text = text
    self.meth = method
    self.pos = pos

  def get_rendered_surface(self):
    return self.digital_font.render(self.text + str(self.meth()), 1, (0,0,0))

  def get_pos(self):
    return self.pos

  def update(self):
    self.digital_font.render(self.text + str(self.meth()), 1, (0,0,0))

def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  slot_machine = SlotMachine(500, 1000)
  spin_results = slot_machine.get_results()
  icon_images = []

  digital_fonts_hash = [
    {"text": "Bet: ", "method": slot_machine.get_bet, "pos": (50, 400)},
    {"text": "Credit: ", "method": slot_machine.get_current_cash, "pos": (160, 400)},
    {"text": "Jackpot: ", "method": slot_machine.get_current_jackpot, "pos": (330, 400)}
  ]
  digital_fonts = pygame.sprite.Group()

  for digital_font in digital_fonts_hash:
    digital_fonts.add(DigitalFont(digital_font["text"], digital_font["method"], digital_font["pos"]))

  BUTTON_BOTTOM_POS = background.get_height() - 150

  distance_between_buttons = 30
  x = 30
  bet_buttons_hash = [
    {"image_name": "ten_button.png", "value": 10},
    {"image_name": "twenty_button.png", "value": 20},
    {"image_name": "fifty_button.png", "value": 50},
    {"image_name": "hundred_button.png", "value": 100}
  ]
  bet_buttons = pygame.sprite.Group()

  for bet_button in bet_buttons_hash:
    slot_machine_btn = SlotMachineButton("images/" + bet_button["image_name"], bet_button["value"], (x, BUTTON_BOTTOM_POS))
    bet_buttons.add(slot_machine_btn)
    x += slot_machine_btn.image.get_width() + distance_between_buttons

  action_buttons_hash = [
    {"image_name": "spin_button.png", "method": slot_machine.spin, "pos": (550, BUTTON_BOTTOM_POS)},
    {"image_name": "reset_button.png", "method": slot_machine.reset, "pos": (670, BUTTON_BOTTOM_POS)}
  ]
  action_buttons = pygame.sprite.Group()

  for action_button in action_buttons_hash:
    action_buttons.add(SlotMachineActionButton("images/" + action_button["image_name"], action_button["method"], action_button["pos"]))

  all_symbols = pygame.sprite.Group()
  icons = slot_machine.get_icons()
  for icon in icons:
    all_symbols.add(icon)

  clock = pygame.time.Clock()

  reel_positions = [(40, 150), (270, 150), (500, 150)]

  for symbol in all_symbols:
    for symbol_name in spin_results:
      if (symbol.name == symbol_name):
        icon_images.append(symbol)

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
        for action_button in action_buttons:
          if(action_button.rect.collidepoint(event.pos)):
            action_button.call_method()
            spin_results = slot_machine.get_results()

            icon_images = []
            for symbol in all_symbols:
              for symbol_name in spin_results:
                if (symbol.name == symbol_name):
                  icon_images.append(symbol)

    screen.blit(background, background.get_rect())

    action_buttons.update()
    for action_button in action_buttons:
      screen.blit(action_button.image, action_button.get_pos())

    digital_fonts.update()
    for digital_font in digital_fonts:
      screen.blit(digital_font.get_rendered_surface(), digital_font.get_pos())

    bet_buttons.update()
    for bet_button in bet_buttons:
      screen.blit(bet_button.image, bet_button.pos)

    for i in range(3):
      screen.blit(icon_images[i].image, reel_positions[i])

    pygame.display.flip()

def main():
  start_game()

if __name__ == "__main__": main()

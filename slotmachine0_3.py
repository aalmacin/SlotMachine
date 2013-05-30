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
    self.image = self.image.convert_alpha()
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
    self.image = self.image.convert_alpha()
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
  MAIN_MSG = "Aldrin's Slot Machine"
  YOU_WIN = "You just won $"
  YOU_WIN_JACKPOT = "Jackpot won $"
  YOU_LOST = "You just lost $"
  YOU_BET = "You bet $"
  NO_CASH_LEFT = "Cannot bet to that amount. Cash not enough."
  CANNOT_SPIN = "Cannot spin. Change bet to a lower value."

  def __init__(self, starting_jackpot, starting_cash):
    pygame.mixer.init()
    self.bet_snd = pygame.mixer.Sound("sounds/bet_snd.wav")
    self.bet_no_cash_snd = pygame.mixer.Sound("sounds/bet_no_cash_snd.wav")
    self.spin_snd = pygame.mixer.Sound("sounds/spin_snd.ogg")
    self.spinning_snd = pygame.mixer.Sound("sounds/spinning_snd.ogg")
    self.reset_snd = pygame.mixer.Sound("sounds/reset_snd.ogg")

    self.JACKPOT_INCREASE_RATE = .15
    self.current_message = SlotMachine.MAIN_MSG

    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash
    self.icons = []
    self.__create_icons()
    self.set_initial_values()

  def set_initial_values(self):
    self.current_jackpot = self.starting_jackpot
    self.current_cash = self.starting_cash
    self.results = 3*["Siete"]
    self.bet = 10
    # TODO turns , wins , loses
    self.turns = 0
    self.wins = 0
    self.loses = 0

  def __create_icons(self):
    self.icons.append(Icon("Sad Face", 0, 0, "sadface.png", bonus_win_rate = 1)) # The win rate is for when no sad face is on the reel
    self.icons.append(Icon("Katipunero Hat", 10, 1, "katipunero_hat.png"))
    self.icons.append(Icon("Bandana", 20, 2, "bandana.png"))
    self.icons.append(Icon("Camesa De Chino", 30, 2, "camesa_de_chino.png"))
    self.icons.append(Icon("Banyal", 100, 2, "banyal.png"))
    self.icons.append(Icon("Tsinelas", 200, 2, "tsinelas.png"))
    self.icons.append(Icon("Arnis", 300, 5, "arnis.png"))
    self.icons.append(Icon("Siete", 1000, 10, "siete.png", bonus_win_rate = 5))

  def set_bet(self, bet):
    if self.current_cash - bet >= 0:
      self.bet = bet
      self.current_message = SlotMachine.YOU_BET + str(self.bet)
      self.bet_snd.play()
    else:
      self.current_message = SlotMachine.NO_CASH_LEFT
      self.bet_no_cash_snd.play()

  def get_bet(self):
    return self.bet

  def get_current_cash(self):
    return self.current_cash

  def get_current_jackpot(self):
    return self.current_jackpot

  def get_icons(self):
    return self.icons

  def spin(self):
    if self.current_cash - self.bet >= 0:
      self.spin_snd.play()
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
    else:
      self.current_message = SlotMachine.CANNOT_SPIN

  def get_current_message(self):
    return self.current_message

  def __pay(self):
    self.current_cash -= self.bet

  def __increase_jackpot(self):
    self.current_jackpot += (int(self.bet * self.JACKPOT_INCREASE_RATE))

  def __check_results(self):
    winnings = 0
    jackpot_won = 0
    for icon in self.icons:
      if self.results.count(icon.name) == 3:
        winnings += self.bet * icon.win_rate_full
        # Play jackpot when 3 of a kind is the result
        jackpot_won = self.jackpot_win()
      if self.results.count(icon.name) == 2:
        winnings += self.bet * icon.win_rate_two
    if self.results.count(self.icons[7].name) == 1:
      winnings += self.bet * self.icons[7].bonus_win_rate
    if self.results.count(self.icons[0].name) == 0:
      winnings += self.bet * self.icons[0].bonus_win_rate

    if jackpot_won > 0:
      self.current_message = SlotMachine.YOU_WIN_JACKPOT + str(jackpot_won) + " With Cash $" + str(winnings)
    elif winnings > 0:
      self.current_cash += winnings
      self.current_message = SlotMachine.YOU_WIN + str(winnings)
    elif winnings <= 0:
      self.current_message = SlotMachine.YOU_LOST + str(self.bet)
    else:
      self.current_message = "Somethings wrong"


  def jackpot_win(self):
    JACKPOT_WILDCARD = 7
    jackpot_try = random.randint(1, 100)
    winnings = 0

    if jackpot_try == JACKPOT_WILDCARD:
      self.current_cash += self.current_jackpot
      winnings = self.current_jackpot
      self.current_jackpot = self.starting_jackpot
    return winnings

  def get_results(self):
    return self.results

  def reset(self):
    self.set_initial_values()
    self.current_message = SlotMachine.MAIN_MSG

"""
  Class: Icon
"""
class Icon(pygame.sprite.Sprite):
  def __init__(self, name, win_rate_full, win_rate_two, icon_image, bonus_win_rate = 0):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.image = pygame.image.load("images/" + icon_image)
    self.image = self.image.convert_alpha()
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
  def __init__(self, method, pos, color = (196,65,46)):
    pygame.sprite.Sprite.__init__(self)
    self.digital_font = pygame.font.Font("fonts/DS-DIGIT.TTF", 22)
    self.font_color = color
    self.meth = method
    self.pos = pos

  def get_rendered_surface(self):
    return self.digital_font.render(str(self.meth()), 1, self.font_color)

  def get_pos(self):
    return self.pos

  def update(self):
    self.digital_font.render(str(self.meth()), 1, self.font_color)

def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  slot_machine = SlotMachine(500, 1000)
  spin_results = slot_machine.get_results()
  icon_images = []

  digital_fonts_hash = [
    {"method": slot_machine.get_bet, "pos": (245, 424)},
    {"method": slot_machine.get_current_cash, "pos": (80, 424)},
    {"method": slot_machine.get_current_jackpot, "pos": (445, 424)},
  ]
  digital_fonts = pygame.sprite.Group()

  current_message_digifont = DigitalFont(slot_machine.get_current_message, (100, 140), (0, 0, 0))

  for digital_font in digital_fonts_hash:
    digital_fonts.add(DigitalFont(digital_font["method"], digital_font["pos"]))

  BUTTON_BOTTOM_POS = background.get_height() - 165

  distance_between_buttons = 30
  x = 70
  bet_buttons_hash = [
  #TODO One Button
    {"image_name": "ten_button.png", "value": 10, "pos": (70, BUTTON_BOTTOM_POS)},
    {"image_name": "twenty_button.png", "value": 20, "pos": (150, BUTTON_BOTTOM_POS)},
    {"image_name": "fifty_button.png", "value": 50, "pos": (480, BUTTON_BOTTOM_POS)},
    {"image_name": "hundred_button.png", "value": 100, "pos": (560, BUTTON_BOTTOM_POS)}
  ]
  bet_buttons = pygame.sprite.Group()

  for bet_button in bet_buttons_hash:
    bet_buttons.add(SlotMachineButton("images/" + bet_button["image_name"], bet_button["value"], bet_button["pos"]))

  spin_button = SlotMachineActionButton("images/spin_button.png" , slot_machine.spin, (270, BUTTON_BOTTOM_POS))
  reset_button = SlotMachineActionButton("images/reset_button.png" , slot_machine.reset, (210, BUTTON_BOTTOM_POS + 30))
  action_buttons = pygame.sprite.Group(spin_button, reset_button)

  all_symbols = pygame.sprite.Group()
  icons = slot_machine.get_icons()
  for icon in icons:
    all_symbols.add(icon)

  clock = pygame.time.Clock()

  reel_positions = [(75, 258), (265, 258), (445, 258)]

  for symbol in all_symbols:
    for symbol_name in spin_results:
      if (symbol.name == symbol_name):
        icon_images.append(symbol)
  start_time = 0
  spinning = False
  prev_results = slot_machine.get_results()

  #Play the bg music
  pygame.mixer.music.load("sounds/background_msc.wav")
  pygame.mixer.music.play(-1)

  prev_bet, prev_jackpot, prev_current_msg, prev_cash = slot_machine.bet, slot_machine.current_jackpot, slot_machine.current_message, slot_machine.current_cash
  def prev_get_bet():
    return prev_bet
  def prev_get_current_cash():
    return prev_cash
  def prev_get_current_jackpot():
    return prev_jackpot
  def prev_get_current_msg():
    return prev_current_msg

  prev_bet_digifont = DigitalFont(prev_get_bet, (245, 424))
  prev_cash_digifont = DigitalFont(prev_get_current_cash, (80, 424))
  prev_jackpot_digifont = DigitalFont(prev_get_current_jackpot, (445, 424))
  prev_message_digifont = DigitalFont(prev_get_current_msg, (100, 140), (0, 0, 0))

  prev_digifonts = pygame.sprite.Group(prev_bet_digifont, prev_jackpot_digifont, prev_cash_digifont, prev_message_digifont)

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
        if(spin_button.rect.collidepoint(event.pos)):
          if not spinning:
            spin_button.call_method()
            spin_results = slot_machine.get_results()

            icon_images = []
            for symbol in all_symbols:
              for symbol_name in spin_results:
                if (symbol.name == symbol_name):
                  icon_images.append(symbol)

            start_time = time.time()
            spinning = True
        elif(reset_button.rect.collidepoint(event.pos)):
          slot_machine.reset_snd.play()
          reset_button.call_method()


    screen.blit(background, background.get_rect())

    action_buttons.update()
    for action_button in action_buttons:
      screen.blit(action_button.image, action_button.get_pos())

    digital_fonts.update()

    bet_buttons.update()
    for bet_button in bet_buttons:
      screen.blit(bet_button.image, bet_button.pos)

    if time.time() - start_time < 1 and spinning:
      for i in range(3):
        screen.blit(prev_results[i].image, reel_positions[i])
      for digital_font in prev_digifonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.get_pos())
    elif time.time() - start_time < 2 and spinning:
      for i in range(3):
        screen.blit(icons[random.randint(0, len(icons) - 1)].image, reel_positions[i])
      slot_machine.spinning_snd.play()
      for digital_font in prev_digifonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.get_pos())
    else:
      for i in range(3):
        screen.blit(icon_images[i].image, reel_positions[i])
      screen.blit(current_message_digifont.get_rendered_surface(), current_message_digifont.get_pos())
      spinning = False
      prev_results = icon_images
      slot_machine.spinning_snd.stop()
      for digital_font in digital_fonts:
        screen.blit(digital_font.get_rendered_surface(), digital_font.get_pos())

      prev_bet, prev_jackpot, prev_current_msg, prev_cash = slot_machine.bet, slot_machine.current_jackpot, slot_machine.current_message, slot_machine.current_cash

    pygame.display.flip()

def main():
  start_game()

if __name__ == "__main__": main()

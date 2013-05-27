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
BACKGROUND_IMAGE_NAME = "background.png"

class SlotMachineButton(pygame.sprite.Sprite):
  def __init__(self, image_name, value):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image_name)
    self.image = self.image.convert()
    self.rect = self.image.get_rect()
    self.value = value

def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  ten_button = SlotMachineButton("ten_button.png", 10)
  twenty_button = SlotMachineButton("twenty_button.png", 20)
  fifty_button = SlotMachineButton("fifty_button.png", 50)
  hundred_button = SlotMachineButton("hundred_button.png", 100)

  button_sprites = pygame.sprite.Group(ten_button, twenty_button, fifty_button, hundred_button)

  clock = pygame.time.Clock()

  continue_playing = True
  while (continue_playing):
    # Tick
    clock.tick(FRAME_RATE)

    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        continue_playing = False

    BUTTON_BOTTOM_POS = background.get_height() - ten_button.image.get_height() - 50

    screen.blit(background, background.get_rect())

    x = 30
    for btn_sprite in button_sprites:
      screen.blit(btn_sprite.image, (x, BUTTON_BOTTOM_POS))
      x += (btn_sprite.image.get_width() + 30)

    pygame.display.flip()

def main():
  start_game()


if __name__ == "__main__": main()

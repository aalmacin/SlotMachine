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

def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  BUTTON_BOTTOM_POS = background.get_height() - 150

  distance_between_buttons = 30
  x = 30
  buttons = [{"image_name": "ten_button.png", "value": 10}, {"image_name": "twenty_button.png", "value": 20}, {"image_name": "fifty_button.png", "value": 50}, {"image_name": "hundred_button.png", "value": 100}]
  button_sprites = pygame.sprite.Group()

  for button in buttons:
    slot_machine_btn = SlotMachineButton(button["image_name"], button["value"], (x, BUTTON_BOTTOM_POS))
    button_sprites.add(slot_machine_btn)
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
        for btn_sprite in button_sprites:
          if(btn_sprite.rect.collidepoint(event.pos)):
            print btn_sprite.get_value()


    screen.blit(background, background.get_rect())

    button_sprites.update()
    for btn_sprite in button_sprites:
      screen.blit(btn_sprite.image, btn_sprite.pos)

    pygame.display.flip()

def main():
  start_game()


if __name__ == "__main__": main()

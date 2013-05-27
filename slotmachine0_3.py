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


def start_game():
  # Assign the Display Variables
  background = pygame.image.load(BACKGROUND_IMAGE_NAME)
  screen = pygame.display.set_mode(background.get_size())
  pygame.display.set_caption(GAME_TITLE)

  clock = pygame.time.Clock()

  continue_playing = True
  while (continue_playing):
    clock.tick(FRAME_RATE)
    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        continue_playing = False

    screen.blit(background, background.get_rect())
    pygame.display.flip()

def main():
  start_game()


if __name__ == "__main__": main()

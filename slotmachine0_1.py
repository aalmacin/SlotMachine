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
from slotmachine import SlotMachine

def main():
  slot_machine = SlotMachine(1000, 500)
  slot_machine.start_game()

if __name__ == "__main__": main()

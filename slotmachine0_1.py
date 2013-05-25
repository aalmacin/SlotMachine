"""
    Author Name: Aldrin Jerome Almacin
    Last Modified by: Aldrin Jerome Almacin
    Date last Modified:
    Program description: A game in which the user bets and pulls the lever to increase his credits.
    Revision History: 0.1
"""
def start_game():
  credits = 1000
  print("Aldrin's slot machine")
  bet = place_bet()

def place_bet():
  while True:
    print("How much do you want to bet?")
    print("10, 20, 100")
    bet = int(raw_input(">>> "))
    if (bet != 10 or bet != 20 or bet != 100): break
  return bet

def get_result():
  print("How much do you want to bet?")

def main():
  start_game()

if __name__ == "__main__": main()

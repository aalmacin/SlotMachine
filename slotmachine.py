class SlotMachine:
  def __init__(self, starting_jackpot, starting_cash):
    self.starting_jackpot = starting_jackpot
    self.starting_cash = starting_cash

  def start_game(self):
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Prev_Bet= 0
    win_number = 0
    loss_number = 0

    bet = self.get_bet()
    results = self.get_results()

  def get_bet(self):
    bet = -1
    possible_bets = "1, 10, 20, 50, 100"
    while (bet not in possible_bets.split(", ")):
      print("How much would you bet?")
      print possible_bets
      bet = raw_input(">>> ")
    return int(bet)

  def get_results(self):
    results = 3*[""]
    for spin in range(3):
      results = []

    return results

class Player:
  def __init__(self, name):
    self.name = name

  def get_name(self):
    return self.name

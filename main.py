from colors import red, yellow, green, blue
import random
import sys

score = 0
fuel = 50
coins = 0
ammo = 5
lasers = 0
bombs = 0
n_coord = 0

grid = ["O", "*", "*", "*", "O", "*", "*", "*", "*", "*", "*", "*", "O", "*", "*", "*", "*", "*", "*", "*", "*", "*", "O", "*", "*", "*", "*", "O", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", red("^"), "*", "*", "*", "O", "*", "*", "O", "*", "*", "*"]
player_pos = "*"


def print_grid():
  global grid
  print(grid[0] + " " + grid[1] + " " + grid[2] + " " + grid[3] + " " + grid[4] + " " + grid[5] + " " + grid[6])
  print(grid[7] + " " + grid[8] + " " + grid[9] + " " +  grid[10] + " " + grid[11] + " " + grid[12] + " " + grid[13])
  print(grid[14] + " " + grid[15] + " " +  grid[16] + " " + grid[17] + " " + grid[18] + " " + grid[19] + " " + grid[20])
  print(grid[21] + " " +  grid[22] + " " +  grid[23] + " " +  grid[24] + " " + grid[25] + " " + grid[26] + " " + grid[27])
  print(grid[28] + " " +  grid[29] + " " +  grid[30] + " " +  grid[31] + " " + grid[32] + " " + grid[33] + " " + grid[34])
  print(grid[35] + " " +  grid[36] + " " +  grid[37] + " " +  grid[38] + " " + grid[39] + " " + grid[40] + " " + grid[41])
  print(grid[42] + " " +  grid[43] + " " +  grid[44] + " " +  grid[45] + " " + grid[46] + " " + grid[47] + " " + grid[48])


def start():
  global ship_x_1
  global ship_y_1
  global coins
  global ammo
  global player_pos
  global score
  global fuel
  global mission
  get_mission()
  check_coins()
  check_merch()
  check_fuel()
  game_over()
  print(str(score) + " Points | " + str(fuel) + " Fuel | " + str(coins) + " Coins | " + str(ammo) + " Ammo | " + mission)
  print()
  print_grid()
  print()
  print("Where would you like to go, commander?")
  get_ship_placement()
  print()
  start()

def get_ship_placement():
  global fuel
  global n_coord
  global score
  ship_move = input("N, E, S, W? ").lower()
  if ship_move == "n":
    move_up()
    fuel -= 1
    n_coord += 1
    score += 1
  if ship_move == "w":
    move_left()
    fuel -= 1
    score += 1
  if ship_move == "e":
    move_right()
    fuel -= 1
    score += 1
  if ship_move == "s":
    move_down()
    fuel -= 1
    n_coord -= 1
    score += 1
  if ship_move == "shoot":
    shoot_ammo()
    
def move_up():
  global player_pos
  grid[48] = grid[48 - 7]
  grid[47] = grid[47 - 7]
  grid[46] = grid[46 - 7]
  grid[45] = player_pos
  grid[44] = grid[44 - 7]
  grid[43] = grid[43 - 7]
  grid[42] = grid[42 - 7]
  grid[41] = grid[41 - 7]
  grid[40] = grid[40 - 7]
  grid[39] = grid[39 - 7]
  grid[38] = red("^")
  player_pos = grid[38 - 7]
  grid[37] = grid[37 - 7]
  grid[36] = grid[36 - 7]
  grid[35] = grid[35 - 7]
  grid[34] = grid[34 - 7]
  grid[33] = grid[33 - 7]
  grid[32] = grid[32 - 7]
  grid[31] = grid[31 - 7]
  grid[30] = grid[30 - 7]
  grid[29] = grid[29 - 7]
  grid[28] = grid[28 - 7]
  grid[27] = grid[27 - 7]
  grid[26] = grid[26 - 7]
  grid[25] = grid[25 - 7]
  grid[24] = grid[24 - 7]
  grid[23] = grid[23 - 7]
  grid[22] = grid[22 - 7]
  grid[21] = grid[21 - 7]
  grid[20] = grid[20 - 7]
  grid[19] = grid[19 - 7]
  grid[18] = grid[18 - 7]
  grid[17] = grid[17 - 7]
  grid[16] = grid[16 - 7]
  grid[15] = grid[15 - 7]
  grid[14] = grid[14 - 7]
  grid[13] = grid[13 - 7]
  grid[12] = grid[12 - 7]
  grid[11] = grid[11 - 7]
  grid[10] = grid[10 - 7]
  grid[9] = grid[9 - 7]
  grid[8] = grid[8 - 7]
  grid[7] = grid[7 - 7]
  grid6 = random.randint(1,22)
  if grid6 <= 2:
    grid[6] = "O"
  elif grid6 == 3:
    grid[6] = green("+")
  elif grid6 == 4:
    grid[6] = blue("3")
  elif grid6 == 5:
    grid[6] = blue("5")
  else:
    grid[6] = "*"
  grid5 = random.randint(1,22)
  if grid5 <= 2:
    grid[5] = "O"
  elif grid5 == 3:
    grid[5] = green("+")
  elif grid5 == 4:
    grid[5] = blue("3")
  elif grid5 == 5:
    grid[5] = yellow("O")
  else:
    grid[5] = "*"
  grid4 = random.randint(1,22)
  if grid4 <= 2:
    grid[4] = "O"
  elif grid4 == 3:
    grid[4] = green("+")
  elif grid4 == 4:
    grid[4] = blue("3")
  elif grid4 == 5:
    grid[4] = blue("5")
  else:
    grid[4] = "*"
  grid3 = random.randint(1,22)
  if grid3 <= 2:
    grid[3] = "O"
  elif grid3 == 3:
    grid[3] = green("+")
  elif grid3 == 4:
    grid[3] = blue("3")
  elif grid3 == 5:
    grid[3] = blue("5")
  else:
    grid[3] = "*"
  grid2 = random.randint(1,22)
  if grid2 <= 2:
    grid[2] = "O"
  elif grid2 == 3:
    grid[2] = green("+")
  elif grid2 == 4:
    grid[2] = blue("3")
  elif grid2 == 5:
    grid[2] = blue("5")
  else:
    grid[2] = "*"
  grid1 = random.randint(1,22)
  if grid1 <= 2:
    grid[1] = "O"
  elif grid1 == 3:
    grid[1] = green("+")
  elif grid1 == 4:
    grid[1] = blue("3")
  elif grid1 == 5:
    grid[1] = yellow("O")
  else:
    grid[1] = "*"
  grid0 = random.randint(1,23)
  if grid0 <= 2:
    grid[0] = "O"
  elif grid0 == 3:
    grid[0] = green("+")
  elif grid0 == 4:
    grid[0] = blue("3")
  elif grid0 == 5:
    grid[0] = blue("5")
  elif grid0 == 6:
    grid[0] = yellow("O")
  else:
    grid[0] = "*"


def check_fuel():
  global player_pos
  global fuel
  if player_pos == blue("3"):
    fuel += 3
    player_pos = "O"
  if player_pos == blue("5"):
    fuel += 5
    player_pos = "O"
  if player_pos == blue("6"):
    fuel += 6
    player_pos = "O"


def move_left():
  global player_pos
  grid[48] = grid[48 - 1]
  grid[47] = grid[47 - 1]
  grid[46] = grid[46 - 1]
  grid[45] = grid[45 - 1]
  grid[44] = grid[44 - 1]
  grid[43] = grid[43 - 1]
  grid[6] = grid[6 - 1]
  grid[41] = grid[41 - 1]
  grid[40] = grid[40 - 1]
  grid[39] = player_pos
  grid[38] = red("<")
  player_pos = grid[38 - 1]
  grid[37] = grid[37 - 1]
  grid[36] = grid[36 - 1]
  grid[5] = grid[5 - 1]
  grid[34] = grid[34 - 1]
  grid[33] = grid[33 - 1]
  grid[32] = grid[32 - 1]
  grid[31] = grid[31 - 1]
  grid[30] = grid[30 - 1]
  grid[29] = grid[29 - 1]
  grid[4] = grid[4 - 1]
  grid[27] = grid[27 - 1]
  grid[26] = grid[26 - 1]
  grid[25] = grid[25 - 1]
  grid[24] = grid[24 - 1]
  grid[23] = grid[23 - 1]
  grid[22] = grid[22 - 1]
  grid[3] = grid[3 - 1]
  grid[20] = grid[20 - 1]
  grid[19] = grid[19 - 1]
  grid[18] = grid[18 - 1]
  grid[17] = grid[17 - 1]
  grid[16] = grid[16 - 1]
  grid[15] = grid[15 - 1]
  grid[2] = grid[2 - 1]
  grid[13] = grid[13 - 1]
  grid[12] = grid[12 - 1]
  grid[11] = grid[11 - 1]
  grid[10] = grid[10 - 1]
  grid[9] = grid[9 - 1]
  grid[8] = grid[8 - 1]
  grid[1] = grid[1 - 1]
  grid0 = random.randint(1,20)
  if grid0 <= 2:
    grid[0] = "O"
  elif grid0 == 3:
    grid[0] = yellow("O")
  elif grid0 == 6:
    grid[0] = yellow("M")
  else:
    grid[0] = "*"
  grid7 = random.randint(1,20)
  if grid7 <= 2:
    grid[7] = "O"
  elif grid7 == 3:
    grid[7] = yellow("O")
  else:
    grid[7] = "*"
  grid14 = random.randint(1,20)
  if grid14 <= 2:
    grid[14] = "O"
  elif grid14 == 3:
    grid[14] = yellow("O")
  else:
    grid[14] = "*"
  grid21 = random.randint(1,20)
  if grid21 <= 2:
    grid[21] = "O"
  elif grid21 == 3:
    grid[21] = yellow("O")
  else:
    grid[21] = "*"
  grid28 = random.randint(1,20)
  if grid28 <= 2:
    grid[28] = "O"
  elif grid28 == 3:
    grid[28] = yellow("O")
  else:
    grid[28] = "*"
  grid35 = random.randint(1,20)
  if grid35 <= 2:
    grid[35] = "O"
  elif grid35 == 3:
    grid[35] = yellow("O")
  else:
    grid[35] = "*"
  grid42 = random.randint(1,20)
  if grid42 <= 2:
    grid[42] = "O"
  elif grid42 == 3:
    grid[42] = yellow("O")
  else:
    grid[42] = "*"



def move_right():
  global player_pos
  grid[0] = grid[0 + 1]
  grid[1] = grid[1 + 1]
  grid[2] = grid[2 + 1]
  grid[3] = grid[3 + 1]
  grid[4] = grid[4 + 1]
  grid[5] = grid[5 + 1]
  grid[7] = grid[7 + 1]
  grid[8] = grid[8 + 1]
  grid[9] = grid[9 + 1]
  grid[10] = grid[10 + 1]
  grid[11] = grid[11 + 1]
  grid[12] = grid[12 + 1]
  grid[14] = grid[14 + 1]
  grid[15] = grid[15 + 1]
  grid[16] = grid[16 + 1]
  grid[17] = grid[17 + 1]
  grid[18] = grid[18 + 1]
  grid[19] = grid[19 + 1]
  grid[21] = grid[21 + 1]
  grid[22] = grid[22 + 1]
  grid[23] = grid[23 + 1]
  grid[24] = grid[24 + 1]
  grid[25] = grid[25 + 1]
  grid[26] = grid[26 + 1]
  grid[28] = grid[28 + 1]
  grid[29] = grid[29 + 1]
  grid[30] = grid[30 + 1]
  grid[31] = grid[31 + 1]
  grid[32] = grid[32 + 1]
  grid[33] = grid[33 + 1]
  grid[35] = grid[35 + 1]
  grid[36] = grid[36 + 1]
  grid[37] = player_pos
  player_pos = grid[38 + 1]
  grid[38] = red(">")
  grid[39] = grid[39 + 1]
  grid[40] = grid[40 + 1]
  grid[42] = grid[42 + 1]
  grid[43] = grid[43 + 1]
  grid[44] = grid[44 + 1]
  grid[45] = grid[45 + 1]
  grid[46] = grid[46 + 1]
  grid[47] = grid[47 + 1]
  grid6 = random.randint(1,20)
  if grid6 <= 4:
    grid[6] = "O"
  elif grid6 == 5:
    grid[6] = yellow("O")
  elif grid6 == 6:
    grid[6] = yellow("M")
  else:
    grid[6] = "*"
  grid13 = random.randint(1,20)
  if grid13 <= 4:
    grid[13] = "O"
  elif grid13 == 5:
    grid[13] = yellow("O")
  else:
    grid[13] = "*"
  grid20 = random.randint(1,20)
  if grid20 <= 4:
    grid[20] = "O"
  elif grid20 == 5:
    grid[20] = yellow("O")
  else:
    grid[20] = "*"
  grid27 = random.randint(1,20)
  if grid27 <= 4:
    grid[27] = "O"
  elif grid27 == 5:
    grid[27] = yellow("O")
  else:
    grid[27] = "*"
  grid34 = random.randint(1,20)
  if grid34 <= 4:
    grid[34] = "O"
  elif grid34 == 5:
    grid[34] = yellow("O")
  else:
    grid[34] = "*"
  grid41 = random.randint(1,20)
  if grid41 <= 4:
    grid[41] = "O"
  elif grid41 == 5:
    grid[41] = yellow("O")
  else:
    grid[41] = "*"
  grid48 = random.randint(1,20)
  if grid48 <= 4:
    grid[48] = "O"
  elif grid48 == 5:
    grid[48] = yellow("O")
  else:
    grid[48] = "*"


def move_down():
  global player_pos
  grid[0] = grid[0 + 7]
  grid[1] = grid[1 + 7]
  grid[2] = grid[2 + 7]
  grid[3] = grid[3 + 7]
  grid[4] = grid[4 + 7]
  grid[5] = grid[5 + 7]
  grid[6] = grid[6 + 7]
  grid[7] = grid[7 + 7]
  grid[8] = grid[8 + 7]
  grid[9] = grid[9 + 7]
  grid[10] = grid[10 + 7]
  grid[11] = grid[11 + 7]
  grid[12] = grid[12 + 7]
  grid[13] = grid[13 + 7]
  grid[14] = grid[14 + 7]
  grid[15] = grid[15 + 7]
  grid[16] = grid[16 + 7]
  grid[17] = grid[17 + 7]
  grid[18] = grid[18 + 7]
  grid[19] = grid[19 + 7]
  grid[20] = grid[20 + 7]
  grid[21] = grid[21 + 7]
  grid[22] = grid[22 + 7]
  grid[23] = grid[23 + 7]
  grid[24] = grid[24 + 7]
  grid[25] = grid[25 + 7]
  grid[26] = grid[26 + 7]
  grid[27] = grid[27 + 7]
  grid[28] = grid[28 + 7]
  grid[29] = grid[29 + 7]
  grid[30] = grid[30 + 7]
  grid[31] = player_pos
  player_pos = grid[38 + 7]
  grid[32] = grid[32 + 7]
  grid[33] = grid[33 + 7]
  grid[34] = grid[34 + 7]
  grid[35] = grid[35 + 7]
  grid[36] = grid[36 + 7]
  grid[37] = grid[37 + 7]
  grid[38 + 7] = player_pos
  player_pos = grid[38 + 7]
  grid[38] = red("v")
  grid[39] = grid[39 + 7]
  grid[40] = grid[40 + 7]
  grid[41] = grid[41 + 7]
  grid42 = random.randint(1,20)
  if grid42 <= 4:
    grid[42] = "O"
  else:
    grid[42] = "*"
  grid43 = random.randint(1,20)
  if grid43 <= 4:
    grid[43] = "O"
  else:
    grid[43] = "*"
  grid44 = random.randint(1,20)
  if grid44 <= 4:
    grid[44] = "O"
  else:
    grid[44] = "*"
  grid45 = random.randint(1,20)
  if grid45 <= 4:
    grid[45] = "O"
  else:
    grid[45] = "*"
  grid46 = random.randint(1,20)
  if grid46 <= 4:
    grid[46] = "O"
  else:
    grid[46] = "*"
  grid47 = random.randint(1,20)
  if grid47 <= 4:
    grid[47] = "O"
  else:
    grid[47] = "*"
  grid48 = random.randint(1,20)
  if grid48 <= 4:
    grid[48] = "O"
  else:
    grid[48] = "*"


def check_coins():
  global player_pos
  global coins
  global score
  if player_pos == yellow("O"):
    player_pos = "*"
    coins += 1
    score += 5


def check_merch():
  global player_pos
  global coins
  global fuel
  global ammo
  merch_num = random.randint(1,3)
  if merch_num == 1:
    if player_pos == yellow("M"):
      print("(0) EXIT")
      print("(1) Buy 5 Fuel - 3 Coins")
      print("(2) Buy 2 Ammo - 6 Coins")
      item = input("What would you like to buy? (0, 1, 2) ")
      if item == "1" and coins >= 3:
        coins -= 3
        fuel += 5
      if item == "2" and coins >= 6:
        coins -= 6
        ammo += 2
  if merch_num == 2:
    if player_pos == yellow("M"):
      print("(0) EXIT")
      print("(1) Buy 1 Fuel - 2 Coins")
      print("(2) Buy 5 Ammo - 12 Coins")
      item = input("What would you like to buy? (0, 1, 2) ")
      if item == "1" and coins >= 2:
        coins -= 2
        fuel += 1
      if item == "2" and coins >= 12:
        coins -= 12
        ammo += 5
  if merch_num == 3:
    if player_pos == yellow("M"):
      print("(0) EXIT")
      print("(1) Buy 20 Fuel - 13 Coins")
      print("(2) Buy 1 Ammo - 5 Coins")
      item = input("What would you like to buy? (0, 1, 2) ")
      if item == "1" and coins >= 13:
        coins -= 13
        fuel += 1
      if item == "2" and coins >= 5:
        coins -= 5
        ammo += 1
    print()

def shoot_ammo():
  global ammo
  global player_pos
  global score
  global battleship_dead
  if ammo > 0 and player_pos == "O":
    if grid[38] == red("^"):
      before1 = grid[31]
      before2 = grid[24]
      if grid[24] == green("+"):
        grid[31] = red("|")
        grid[24] = red("X")
        coin_or_no = random.randint(0,1)
        score += 100
        if coin_or_no == 1:
          before2 = yellow("O")
        else:
          before2 = "*"
      elif grid[31] == green("+"):
        grid[31] = red("X")
        score += 100
        coin_or_no = random.randint(0,1)
        if coin_or_no == 1:
          before1 = yellow("O")
        else:
          before1 = "*"
          before2 = "*"
      elif grid[31] == green("O"):
        grid[31] = yellow("O")
        grid[30] = yellow("O")
        grid[32] = yellow("O")
        before1 = yellow("O")
        before2 = yellow("O")
        score += 250
        battleship_dead = True
      elif grid[24] == green("O"):
        grid[24] = yellow("O")
        grid[23] = yellow("O")
        grid[25] = yellow("O")
        before1 = yellow("O")
        before2 = yellow("O")
        score += 250
        battleship_dead = True
      else:
        grid[31] = red("|")
        grid[24] = red("|")
      print()
      print_grid()
      print()
      input("Press Enter to Continue ")
      grid[31] = before1
      grid[24] = before2
    if grid[38] == red("<"):
      before1 = grid[37]
      before2 = grid[36]
      if grid[36] == green("+") or grid[36] == green("O"):
        grid[37] = red("-")
        grid[36] = red("X")
        score += 100
        coin_or_no = random.randint(0,1)
        if coin_or_no == 1:
          before2 = yellow("O")
        else:
          before2 = "*"
      elif grid[37] == green("+"):
        grid[37] = red("X")
        score += 100
        coin_or_no = random.randint(0,1)
        if coin_or_no == 1:
          before1 = yellow("O")
        else:
          before1 = "*"
          before2 = "*"
      elif grid[36] == green("O"):
        grid[36] = yellow("O")
        grid[37] = yellow("O")
        grid[35] = yellow("O")
        before1 = yellow("O")
        before2 = yellow("O")
        score += 250
        battleship_dead = True
      else:
        grid[37] = red("-")
        grid[36] = red("-")
      print()
      print_grid()
      print()
      input("Press Enter to Continue ")
      grid[37] = before1
      grid[36] = before2
    if grid[38] == red(">"):
      before1 = grid[39]
      before2 = grid[40]
      if grid[40] == green("+"):
        grid[39] = red("-")
        grid[40] = red("X")
        score += 100
        coin_or_no = random.randint(0,1)
        if coin_or_no == 1:
          before2 = yellow("O")
        else:
          before2 = "*"
      elif grid[39] == green("+"):
        grid[39] = red("X")
        score += 100
        coin_or_no = random.randint(0,1)
        if coin_or_no == 1:
          before1 = yellow("O")
        else:
          before1 = "*"
          before2 = "*"
      elif grid[40] == green("O"):
        grid[40] = yellow("O")
        grid[39] = yellow("O")
        grid[41] = yellow("O")
        before1 = yellow("O")
        before2 = yellow("O")
        score += 250
        battleship_dead = True
      else:
        grid[40] = red("-")
        grid[39] = red("-")
      print()
      print_grid()
      print()
      input("Press Enter to Continue ")
      grid[39] = before1
      grid[40] = before2
    ammo -= 1


def game_over():
  global player_pos
  global fuel
  global score
  if player_pos == green("+") or player_pos == green("=") or player_pos == green("O") or fuel == 0:
    print()
    print(red("GAME OVER"))
    print()
    print("FINAL SCORE - " + str(score) + " Points")
    sys.exit()

mission = "Max"

def get_mission():
  global mission
  global n_coord
  cur_mission = random.randint(1,1)
  if cur_mission == 1:
    battleship()
    mission_coord = 50 - n_coord
    mission = "Kill the Enemy Battleship " + str(mission_coord) + "M N"
    if mission_coord == 0:
      grid[2] = green("=")
      grid[3] = green("O")
      grid[4] = green("=")
      vuln = random.randint(1,2)
      if vuln == 1:
        grid[1] = "O"
      if vuln == 2:
        grid[5] = "O"
      if battleship_dead == True:
        n_coord = 0
        cur_mission = random.randint(1,1)
  if cur_mission == 2:
    battleship()
    mission_coord = 50 - n_coord
    mission = "Destroy the Enemy Battleship " + str(mission_coord) + "M N"
    if mission_coord == 0:
      grid[2] = green("=")
      grid[3] = green("O")
      grid[4] = green("=")
      vuln = random.randint(1,2)
      if vuln == 1:
        grid[1] = "O"
      if vuln == 2:
        grid[5] = "O"
      if battleship_dead == True:
        n_coord = 0
        cur_mission = random.randint(1,1)

battleship_dead = False

def battleship():
  global battleship_dead
  if grid[31] == green("O"):
    grid[37] = green("+")
    grid[39] = green("+")
    grid[38 + 7] = green("+")
  if grid[36] == green("O"):
    grid[38 - 7] = green("+")
    grid[38 + 1] = green("+")
    grid[38 + 7] = green("+")
  if grid[40] == green("O"):
    grid[37] = green("+")
    grid[39] = green("+")
    grid[38 + 7] = green("+")



def begin_program():
  print("Welcome, commander!")
  print()
  tut_ornah = input("Would you like a rundown on the controls? (Y, N) ").lower()
  if tut_ornah == "y":
    print()
    input(blue("Collect blue items to gain fuel "))
    print()
    input(yellow("Collect yellow items to gain coins "))
    print()
    input(green("Avoid green enemies... or else! "))
    print()
    input("Shoot " + green("enemies ") + "from asteroids to destroy them ")
    print()
    input("Fly to " + yellow("M ") + "to exchange your coins for " + red("weapons") + " and " + blue("fuel  "))
    print()
    input("Ready, commander? ")
    start()
  else:
    print()
    start()



begin_program()
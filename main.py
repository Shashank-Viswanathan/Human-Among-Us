from colorama import Fore
import random, time

sabotages = ["Nuclear Meltdown", "Oxygen Depletion", "Comms"]
Start = 0.0
clear = True
completed_tasks = 0
tasks = ["Roll on the ground", "Check Logs", "Open Closet", "Jump 10 times", "Look in Bathroom", "Sit down for thirty seconds", "Find 5 different objects that you can pick up", "Crab Walk for 30 seconds", "Bump into someone", "Touch your toes", "Touch 4 walls", "Touch a door", "Look at a light"]
each_tasks = dict()
displayTasks = ""
checks = 0
game = True
player_roles = dict()
roles = list()
player_count = int(input(Fore.WHITE + "How many players are there? "))
crew_win_tasks = int(input("How many tasks must each crewmate complete to win?"))
players = list()
all_votes = dict()
for i in range(player_count):
  player_name = input(Fore.WHITE+"\nWhat is player " + str(i+1) + " \'s name? ")
  players.append(player_name)
  all_votes[player_name] = 0
all_votes["SKIP"] = 0
imp_count = int(input(Fore.WHITE + "\nHow many imposters are there? "))
crew_win_tasks = crew_win_tasks * (player_count - imp_count)
for i in range(imp_count):
  roles.append("Imposter")
for i in range(player_count-imp_count):
  roles.append("Crewmate")
start = input("\nPress ENTER to assign roles\n")
for player in players:
  start = input(Fore.WHITE+"\nPress ENTER to assign role for " + player)
  role = random.choice(roles)
  roles.remove(role)
  player_roles[player] = role
  if role == "Imposter":
    print(Fore.RED + player + " is an " + role, end='\r')
    time.sleep(1)
    print(Fore.GREEN+"Complete........")
  else:
    print(Fore.BLUE + player + " is a " + role, end='\r')
    time.sleep(1)
    print(Fore.GREEN+"Complete........")
#tasks set up
if crew_win_tasks != 0:
  tasks_per = crew_win_tasks;
  for player in players:
    if player_roles[player] == "Crewmate":
      for i in range(tasks_per):
        displayTasks += random.choice(tasks) + ", "
      each_tasks[player] = displayTasks
      for check_player in each_tasks:
        each_tasks[check_player] = each_tasks[player].split(",")
    else:
      each_tasks[player] = "KILL"
#imp_sabotage_win = int(input(Fore.WHITE+"\nHow many seconds should a sabotage by the imposter be? (Multiple of 5) "))
start = input(Fore.WHITE+"\nPress ENTER to start the game")
print(Fore.RED+"\nThere are " + str(imp_count) + " imposter(s) among us...")
#game
while game:
  for vote in all_votes:
    all_votes[vote] = 0
  clear = True
  voting = True
  #end = time.time()
  #sabotage = float(Start) - float(end)
  #if sabotage == 60:
    #print(Fore.RED + "Imposter has sabotaged " + random.choice(sabotages))
    #Start = time.time()
    #start = input(Fore.RED+"\nPress ENTER to stop sabotage...FAST...")
    #end = time.time()
    #if float(end) - float(start) >= imp_sabotage_win:
      #time.sleep(5)
      #print(Fore.RED+"\nImposters Win!")
      #for check_player in player_roles:
        #if player_roles[check_player] == "Imposter":
          #print(Fore.RED + check_player + " was an imposter")
    #else:
      #print(Fore.GREEN+"Sabotage stopped!\n")
  if crew_win_tasks != 0:
    print(Fore.BLUE+"\n"+str(len(players)-imp_count) + " crewmates remaining\n" + Fore.RED+str(imp_count) + " imposter(s) remaining\n"+Fore.GREEN+"Tasks Completed: " + str(int((completed_tasks/crew_win_tasks)*100)) + "%")
  else:
    print(Fore.BLUE+"\n"+str(len(players)-imp_count) + " crewmates remaining\n" + Fore.RED+str(imp_count) + " imposter(s) remaining\n"+Fore.GREEN+"Tasks Completed: 0%")
  menu = input(Fore.YELLOW+"Scroll through this to check logs. Would you like to report a body?(b), do you want to call an emergency meeting?(e), do you want to check you tasks?(c), or do you want to submit a task?(s). \n") #(S) to sabotage as imposter!
  print("\033[2A")
  print(Fore.LIGHTCYAN_EX+"************(encrypted)************")
  clear = False
  if menu == "b":
    body = input("\nWho was the body? ")
    print(Fore.RED + "Dead Body Reported")
    print(Fore.RED + body + " was killed")
    players.remove(body)
    if imp_count == (len(players)-imp_count):
      time.sleep(5)
      print(Fore.RED+"\nImposters Win!")
      for check_player in player_roles:
        if player_roles[check_player] == "Imposter":
          print(Fore.RED + check_player + " was an imposter")
      exit()
    print(Fore.RED+"\nEmergency meeting called")
    print(Fore.YELLOW+"Discuss and vote...")
    start = input()
    for player in players:
      vote = input(Fore.WHITE+player + " votes ")
      print("\033[2A")
      print(Fore.GREEN+"Complete........")
      all_votes[vote] += 1
    time.sleep(3)
    for check_vote in all_votes:
      checks = 0
      for other_votes in all_votes:
        if all_votes[other_votes] >= all_votes[check_vote]:
          if other_votes != check_vote:
            break
          checks += 1
          continue
        else:
          if checks == len(players):
            print(all_votes)
            if check_vote != "SKIP":
              print(Fore.YELLOW+"\n" + check_vote + " was ejected...")
              time.sleep(1)
              if player_roles[check_vote] == "Imposter":
                print(Fore.RED + check_vote + " was an imposter")
                imp_count -= 1
                players.remove(check_vote)
                checks = 0
                voting = False
                break
              else:
                print(Fore.BLUE + check_vote + " was a crewmate")
                players.remove(check_vote)
                checks = 0
                voting = False
                break
            elif check_vote == "SKIP":
              time.sleep(1)
              print(Fore.YELLOW+"No one was ejected(Skipped)")
              checks = 0
              voting = False
              break
            else:
              voting = "tied"
              break
          else:
            checks += 1
            continue
      if voting == True:
        continue
      else:
        break
    if voting == "tied":
      time.sleep(1)
      print(Fore.YELLOW+"No one was ejected(Tie)")
      checks = 0
    else:
      continue
  #emergency meeting
  elif menu == "e":
    print(Fore.RED+"\nEmergency meeting called")
    print(Fore.YELLOW+"Discuss and vote...")
    start = input()
    for player in players:
      vote = input(Fore.WHITE+player + " votes ")
      print("\033[2A")
      print(Fore.GREEN+"Complete........")
      all_votes[vote] += 1
    time.sleep(3)
    for check_vote in all_votes:
      checks = 0
      for other_votes in all_votes:
        if all_votes[other_votes] >= all_votes[check_vote]:
          if other_votes != check_vote:
            break
          checks += 1
          continue
        else:
          if checks == len(players):
            print(all_votes)
            if check_vote != "SKIP":
              print(Fore.YELLOW+"\n" + check_vote + " was ejected...")
              time.sleep(1)
              if player_roles[check_vote] == "Imposter":
                print(Fore.RED + check_vote + " was an imposter")
                imp_count -= 1
                players.remove(check_vote)
                checks = 0
                voting = False
                break
              else:
                print(Fore.BLUE + check_vote + " was a crewmate")
                players.remove(check_vote)
                checks = 0
                voting = False
                break
            elif check_vote == "SKIP":
              time.sleep(1)
              print(Fore.YELLOW+"No one was ejected(Skipped)")
              checks = 0
              voting = False
              break
            else:
              voting = "tied"
              break
          else:
            checks += 1
            continue
      if voting == True:
        continue
      else:
        break
    if voting == "tied":
      time.sleep(1)
      print(Fore.YELLOW+"No one was ejected(Tie)")
      checks = 0
    else:
      continue
  #check tasks
  elif menu == "c":
    if crew_win_tasks != 0:
      checker = input(Fore.WHITE+"Whose tasks do you want to check? ")
      print("\033[2A")
      print("Next Task: " + each_tasks[checker][0] + ".................", end = '\r')
      start = input()
      #print("\033[2A")
      print("\033[2A")
      print(Fore.YELLOW+checker + " checked their tasks................................")
    else:
      checker = input(Fore.WHITE+"Whose tasks do you want to check? ")
      if player_roles[checker] == "Imposter":
        print("\033[2A")
        print(Fore.RED+"KILL😈...................................")
        start = input()
        #print("\033[2A")
        print("\033[2A")
        print(Fore.YELLOW+checker + " checked their tasks....................................")
      else:
        print("\033[2A")
        print(Fore.YELLOW+random.choice(tasks) + "....................................")
        start = input()
        #print("\033[2A")
        print("\033[2A")
        print(Fore.YELLOW+checker + " checked their tasks..........................................")
  elif menu == "s":
    submitter = input(Fore.WHITE+"\nWho is submitting a task? ")
    if player_roles[submitter] == "Imposter":
      print(Fore.RED+"Hacking...", end="\r")
      time.sleep(1)
      print(Fore.GREEN + submitter + " submitted a task...")
    else:
      if player_roles[submitter] == "Crewmate":
        print(Fore.GREEN + submitter + " submitted a task...")
        each_tasks[submitter].remove(each_tasks[submitter][0])
        completed_tasks += 1
  #elif menu == "S":
    #Start = time.time()
  #Win, lose or continue
  if imp_count == 0 or int((completed_tasks/crew_win_tasks)*100) == 100:
    time.sleep(5)
    print(Fore.BLUE+"\nCrewmates Win!")
    exit()
  elif imp_count == (len(players)-imp_count):
    time.sleep(5)
    print(Fore.RED+"\nImposters Win!")
    for check_player in player_roles:
      if player_roles[check_player] == "Imposter":
        print(Fore.RED + check_player + " was an imposter")
    exit()

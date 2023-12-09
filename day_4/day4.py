
with open("input.txt") as f:
  input = f.readlines()
  input = [l.strip("\n") for l in input]
  
  sol = 0
  for card in input:
    win_nr = []
    play_nr = []
    numbers = card.split(": ")[1]
    
    numbers = numbers.split(" | ")
    
    winning = numbers[0].split(" ")
    
    for nr in winning:
      if nr != "":
        win_nr.append(int(nr))
    
    playing = numbers[1].split(" ")
    for play in playing:
      if play != "":
        play_nr.append(int(play))
    
    wins = 0
    for nr in play_nr:
      if win_nr.__contains__(nr):
        wins += 1
    
    if wins > 0:
      sol = sol + 2**(wins-1)
  
  print(sol)
    
      
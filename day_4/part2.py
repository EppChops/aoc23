
with open("input.txt") as f:
  input = f.readlines()
  input = [l.strip("\n") for l in input]
  
  card_dict = dict()
  for i, card in enumerate(input):
    card_dict.update({(i+1): 1})
  
  for i, card in enumerate(input):
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
    
    for nr in range(wins):
      curr_wins = card_dict.get(i+1)
      card_to_update = i+2+nr
      new_card_curr_wins = card_dict.get(card_to_update)
      card_dict.update({card_to_update: new_card_curr_wins + 1*curr_wins})
  
  sol = 0
  for k,v in card_dict.items():
    sol = sol + v
  
  print(sol)
    
    
  
    
      
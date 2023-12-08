
with open("input.txt") as f:
  input = f.readlines()
  input = [l.strip("\n") for l in input]
  
  symbols = []
  numbers = dict()
  
  for i in range(len(input)):
    j = 0
    while j < len(input[i]):
      if input[i][j] != ".":
        if not input[i][j].isdigit():
          row = i
          col = j
          symbols.append((row, col))
          j += 1
        else:
          num = ""
          row = i
          col = j
          while j < len(input[i]) and input[i][j].isdigit():
            num = num + input[i][j]
            j += 1
          numbers.update({(row, col) : num})
      else:
        j += 1
      
      
  sol = 0
  for (row, col),v in numbers.items():
    areaAround = [(row-1, col - 1 + c) for c in range(len(v)+2)] + [(row + 1, col-1 + c)  for c in range(len(v)+2)] + [(row, col-1), (row, col+len(v))]
    for area in areaAround:
      if symbols.__contains__(area):
        sol = sol + int(v)
        break
  
  print(sol)
        
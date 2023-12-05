import numpy as np

with open("input.txt") as f:
  lines = f.readlines()
  sumPossible = 0
  for i, game in enumerate(lines):
    g = game.split(": ")
    set = g[1].split("; ")
    flag = False
    maxRed = 1
    maxGreen = 1
    maxBlue = 1
    for cubestring in set:
      cubes = cubestring.split(", ")
      for cube in cubes:
        if "red" in cube:
          if int(cube.split(" ")[0]) > maxRed:
            maxRed = int(cube.split(" ")[0])
        if "green" in cube:
          if int(cube.split(" ")[0]) > maxGreen:
            maxGreen = int(cube.split(" ")[0])
        if "blue" in cube:
          if int(cube.split(" ")[0]) > maxBlue:
            maxBlue = int(cube.split(" ")[0])
    
    power = maxRed * maxGreen * maxBlue
    sumPossible += power  
    
  print(sumPossible)
  


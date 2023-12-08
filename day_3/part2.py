
with open("input.txt") as f:
  input = f.readlines()
  input = [l.strip("\n") for l in input]
  
  symbols = []
  numbers = dict()
  
  for i in range(len(input)):
    j = 0
    while j < len(input[i]):
      if input[i][j] == "*":
        row = i
        col = j
        symbols.append((row, col))
        j += 1
      elif input[i][j].isdigit():
        num = ""
        row = i
        col = j
        while j < len(input[i]) and input[i][j].isdigit():
          num = num + input[i][j]
          j += 1
        for c in range(len(num)):
          numbers.update({(row, col + c) : num})
      else:
        j += 1
      
      
  sol = 0
  for (row, col) in symbols:
    areaAround = [(row-1, col-1 + c) for c in range(3)] + [(row+1, col-1 + c) for c in range(3)] + [(row,col-1), (row,col+1)]
    nums = []
    for area in areaAround:
      if numbers.keys().__contains__(area):
        if not nums.__contains__(numbers.get(area)):
          nums.append(numbers.get(area))
    
    
    if len(nums) == 2:
      sol = sol + int(nums[0])*int(nums[1])

  print(sol)
  
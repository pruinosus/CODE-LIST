def sumOfThreeDistinctSquares(n):
  for i in range(n + 1):
      for j in range(i, n + 1):
          for k in range(j, n + 1):
              if i**2 + j**2 + k**2 == n and i != j and j != k and i != k:
                  return True
  
  return False

for n in range(20, 31):
    print(n, sumOfThreeDistinctSquares(n))

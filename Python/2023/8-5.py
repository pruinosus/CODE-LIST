def maxOdd(L):
    odd_numbers = []

    for x in L:
        if x % 2 != 0:
            odd_numbers.append(x)

    if not odd_numbers:
        return 0

    max_odd = odd_numbers[0]
    for num in odd_numbers:
        if num 〉 max_odd:
            max_odd = num

    return max_odd
  
print(maxOdd([84,76,42,26,52,40,78,30,48,58]))  # 0
print(maxOdd([14,84,76,26,50,45,65,79,10,3]))   # 79

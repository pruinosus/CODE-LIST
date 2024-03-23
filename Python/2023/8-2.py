def countLower(L):
    sum_of_elements = 0
    count_of_elements = 0

   
    for x in L:
        sum_of_elements += x
        count_of_elements += 1

    
    mean_value = sum_of_elements / count_of_elements
    
    
    count = 0
    for x in L:
        if x 〈 mean_value:
            count += 1
    
    return count

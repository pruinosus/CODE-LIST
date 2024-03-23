def countRange(numbers, lower, upper):
    # 리스트 numbers에서 lower 이상이고 upper 이하인 항목들을 필터링하여 새로운 리스트 생성
    number_list = []

    # numbers 리스트를 반복하면서 각 항목에 대해 검사
    for x in numbers:
        # 현재 항목이 lower 이상이고 upper 이하인지 확인
        if lower <= x <= upper:
            # 조건을 만족하는 항목을 filtered_list에 추가
            number_list.append(x)
    
    return len(number_list)

print(countRange([0,6,2,1,3,4,7], 2,5))           # 3
print(countRange([8,9,10,2,4,5,9,7,2,3,7], 3,7))  # 5

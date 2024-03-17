#정수 리스트를 매개변수로 입력받아 리스트의 각 항목들 가운데 가장 작은 수를 반환하는 함수 findMin()를 작성하여라.

def findMin(numbers):
    # 입력 리스트의 길이 확인
    length = len(numbers)

    # 리스트가 비어있으면 None 반환
    if length == 0:
        return None

    return min(numbers)
#동작 확인
print(findMin([7,8,3,4,3,6]))        # 3
print(findMin([3,5,7,2,7,2,3,8,6]))  # 2

#$정수들의 리스트 a를 매개변수로 입 력 받아 각 항목을 제곱한 값을 저장한 새로운 리스트를 만들어 반환하는 함수 square()를 작성하여라

def square(a):
    # 각 항목을 제곱한 새로운 리스트 생성
    squared_list = [x**2 for x in a]
    return squared_list

L = [7,6,3,1,5,8,2,4]
print(square(L))  # [49,36,9,1,25,64,4,16]
print(L)          # [7,6,3,1,5,8,2,4]

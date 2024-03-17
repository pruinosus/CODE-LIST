#정수들의 리스트를 읽어서 리스트 내에 포함된 수 가운데 가장 큰 수의 출현 빈도를 출력하는 함수 maxFrequence를 작성하여라.
#예를 들어 리스트가 [1, 2, 6, 4, 8, 8, 3, 9, 12, 7, 12, 12]인 경우 12가 가장 크고 발생 빈도는 세 번이므로 3을 출력한다

def maxFrequence(numbers):
    # 입력 리스트가 비어있으면 None 반환
    if not numbers:
        return None

    # 리스트에서 가장 큰 수 찾기
    max_number = max(numbers)

    # 가장 큰 수의 출현 빈도 계산
    frequency = numbers.count(max_number)

    return frequency

# 테스트
print(maxFrequence ([5,5,5,1,2,3,4,5,4,3,5,5,4,3,3,3,3,3,4])) 
print(maxFrequence ([1,2,1,2,1,4,3,4,3,6,5,6,7])) 

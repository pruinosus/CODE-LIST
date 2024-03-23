#하나의 양의 정수 n을 입력받아 피보나치 수열의 처음 n개로 이루어진 리스트를 반환하는 합수 fibonacci()를 작성하여라.

def fibonacci(n):
    b = [None] * n

    # 초기값 설정
    b[0] = 1
    b[1] = 1

    # 나머지 항목 계산
    for i in range(2, n):
        b[i] = b[i-1] + b[i-2]

    return b

print(fibonacci(5))   # [1,1,2,3,5]
print(fibonacci(10))  # [1,1,2,3,5,8,13,21,34,55]

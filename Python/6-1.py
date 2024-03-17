#두 개의 정수 a와 b(a<=b)를 매개변수로 입력받아 a부터 b까지 모든 숫자의 합을 구하는 함수 sunNumbers()를 작성하여라.

def sumNumbers(a, b):
    # a부터 b까지의 모든 숫자의 합을 계산
    total = sum(range(a, b + 1))
    return total

# 코드실행
print(sumNumbers(5,10))    # 45
print(sumNumbers(15,100))  # 4945

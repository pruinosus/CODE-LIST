#n!(팩토리얼, factorial)이란 1부터 n까지의 모든 정수를 곱한 값을 의미한다. 
#하나의 정수를 매개변수로 입력받아 팩토리얼 값을 반환하는 함수 factorial()을 작성하여라

def factorial(n):
    # n!을 계산하여 반환
    result = 1
    #n + 1 값을 반복에 포함시키기 위해 n+1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(8))   # 40320
print(factorial(12))  # 479001600

#e^x를 근사적으로 계산하기 위한 다음의 수열식을 
#for 반복문을 이용하여 구하는 함수 exponential()을 작성하라. 
#함수는 실수 x를 입력받아 e^x를 반환한다.
#다음 수열식을 이용해 코드를 다시작성해줘 e^x=1+x+(x^2/2!)+(x^3/4!)+(x^4/4!)+...+(e^100/100!)

def exponential(x, terms=100):
    result = 1.0  # 초기값은 n=0일 때의 항
    term = 1.0

    # 주어진 수열식을 이용하여 e^x를 근사적으로 계산
    for n in range(1, terms):
        term *= x / n
        result += term

    return result

# 테스트
x_value = 2.0
result = exponential(x_value)
print(result)  # e^2에 대한 근사값

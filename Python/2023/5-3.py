#세 개의 정수 lower, upper, n을 매개변수로 입력받아 n이 lower와 upper 사이에 
#있는지(lower <= n <= upper)를 검사하는 함수 withinInterval()을 작성하라. 
#이때 입력되는 lower의 값은 항상 upper 보다 작거나 같다고 가정한다.

#앞에서 정의한 withinInterval() 함수를 이용하여 7개의 정수 lower, upper, n1, n2, n3, n4, n5를 입력받아 
#숫자 n1, n2, n3, n4, n5 가운데 단 3개의 값만이 lower와 upper 사이에 속해 있는가를 검사하는 
#함수 exacltyThreeWithinInterval()을 작성하여라. 5개의 값들 가운데 단지 3개의 숫자만이 1ower와 upper 사이에 속해 있으면 True를, 
#아니면 False를 반환하도록 프로그램을 완성하여라.



def withinInterval(lower, upper, n):
    return lower <= n <= upper

def exactlyThreeWithinInterval(lower, upper, first, second, third, fourth, fifth):
    # 주어진 숫자들 중 lower와 upper 사이에 속한 개수를 카운트
    # withinInterval()true이면 1을 반환한 값을 더해서 저장
    count_within_interval = sum([withinInterval(lower, upper, first),
                                 withinInterval(lower, upper, second),
                                 withinInterval(lower, upper, third),
                                 withinInterval(lower, upper, fourth),
                                 withinInterval(lower, upper, fifth)])

    # 정확히 세 개의 숫자가 lower와 upper 사이에 속하는지를 판단
    # 3개의 true가있으면 성립
    return count_within_interval == 3

#동작확인
print(type(withinInterval(1,5,0)))  # <class 'bool'>
print(withinInterval(1, 5, 0))   # False
print(withinInterval(1, 5, 1))   # True
print(withinInterval(1, 5, 3))   # True
print(withinInterval(1, 5, 5))   # True
print(withinInterval(1, 5, 6))   # False

print("==============================================")

print(exactlyThreeWithinInterval(1,5, 1,0,6,5,3))  # True
print(exactlyThreeWithinInterval(1,5, 6,1,0,3,5))  # True
print(exactlyThreeWithinInterval(1,5, 6,1,0,7,2))  # False
print(exactlyThreeWithinInterval(1,5, 6,7,0,1,2))  # False

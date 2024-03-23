#2차원 좌표상에서 점의 위치가 2사분면에 속해 있는지를 검사하는 함수 inSecondQuadrant(x,y)를 구현하여라. 
#점의 좌표 (x,y)를 매개변수로 입력받고, 부울형으로 반환한다. 
#점이 축 위에 위하는 경우 False를 반환한다. "True"나 "False"처럼 문자열을 반환하지 않도록 주의한다.

#앞에서 정의한 inSecondQuadrant() 함수를 이용하여 점들의 좌표 세 개를 입력받아, 
#그중 단지 두 개의 점만 2사분면에 속해 있는지를 검사하는 함수 exactlyTwoSecondQuadrant()를 작성하여라. 
#이때 입력되는 매개변수 x1, y1, x2, y2, x3, y3은 각각 세 점의 좌표 (x1, y1), (x2, y2), (x3, y3)을 의미한다. 
#세개의 점들 가운데 정확히 두개만 2사분면에 위치하면 True를 아니면 Flase를 반환한다.

def inSecondQuadrant(x, y):
    # 점이 축 위에 있는 경우 False 반환
    if x == 0 or y == 0:
        return False
    # x가 음수이고, y가 양수인 경우에만 True 반환
    return x 〈 0 and y 〉 0

def exactlyTwoSecondQuadrant(x1, y1, x2, y2, x3, y3):
    # 각 점이 2사분면에 속하는지 검사
    is_in_second_quadrant1 = inSecondQuadrant(x1, y1)
    is_in_second_quadrant2 = inSecondQuadrant(x2, y2)
    is_in_second_quadrant3 = inSecondQuadrant(x3, y3)

    # 정확히 두 개의 점이 2사분면에 속하는지 판단
    # true일경우 1을 반환
    count_second_quadrant = sum([is_in_second_quadrant1, is_in_second_quadrant2, is_in_second_quadrant3])

    #모든 sum함수로 더한값이 2이면 2사분면에위치한다고 판단
    return count_second_quadrant == 2

# 테스트
print(inSecondQuadrant(-1,2))       # True
print(inSecondQuadrant(-1,-2))      # False
print(inSecondQuadrant(1,-2))       # False
print(inSecondQuadrant(-1,0))       # False

print("==============================================")

print(exactlyTwoSecondQuadrant(-1,2, 2,1, -2,1))   # True
print(exactlyTwoSecondQuadrant(1,2, -2,1, -3,3))   # True
print(exactlyTwoSecondQuadrant(1,2, -2,-1, -2,1))  # False
print(exactlyTwoSecondQuadrant(-1,2, -2,1, -2,2))  # False
print(exactlyTwoSecondQuadrant(1,2, -2,-1, 2,-2))  # False

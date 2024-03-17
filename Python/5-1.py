#2차원 평면상의 세 점의 좌표 (x1, y1), (x2, y2), (x3, y3)을 의미하는 6개의 매개변수 
#x1, y1, x2, y2, x3, y3을 입력받아 세점을 잇는 선분들이 
#직각 삼각형을 이루는지를 검사하는 함수 rightAngled()를 작성하라.

import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def rightAngled(x1, y1, x2, y2, x3, y3):
    # 각 변의 길이 계산
    side1 = calculate_distance(x1, y1, x2, y2)
    side2 = calculate_distance(x2, y2, x3, y3)
    side3 = calculate_distance(x1, y1, x3, y3)

    # 각 변의 길이를 제곱하여 오름차순 정렬
    sides_squared = sorted([side1**2, side2**2, side3**2])

    # 피타고라스의 정리를 이용하여 직각 삼각형인지 검사
    is_right_angled = sides_squared[0] + sides_squared[1] == sides_squared[2]

    return is_right_angled

#동작확인
x1, y1 = 0, 0
x2, y2 = 0, 3
x3, y3 = 4, 0

result = rightAngled(x1, y1, x2, y2, x3, y3)
print(result)  # 값이 맞다면 True출력 

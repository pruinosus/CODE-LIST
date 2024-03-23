#2차원 평 면에서 두 개의 원이 서로 만나는 교점의 개수틀 반환하는 함수 intersect()를 작성하여라.

def intersect(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 간의 거리 계산
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 두 원의 반지름의 합과 중심 간 거리를 비교하여 교점 개수 결정
    if distance < r1 + r2:
        # 두 원이 서로 교차하면 두 교점이 존재
        return 2
    elif distance == r1 + r2:
        # 두 원이 외접하면 한 교점이 존재
        return 1
    else:
        # 두 원이 완전히 겹치지 않거나, 하나가 다른 원 안에 있을 때 교점이 없음
        return 0

# 동작확인
result = intersect(0, 0, 3, 4, 0, 3)
print(result)  # 2  # 두 원이 교차하여 두 교점이 존재

result = intersect(0, 0, 3, 8, 0, 3)
print(result)  # 0  # 두 원이 겹치지 않아 교점이 없음

result = intersect(0, 0, 3, 6, 0, 3)
print(result)  # 1  # 두 원이 외접하여 한 교점이 존재

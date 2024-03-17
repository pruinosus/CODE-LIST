#정수들로 구성된 리스트 a를 매개변수로 입력받아 각 항목들에 대해서 +와 — 연산을 번갈아 수행하는 함수 alternatingSum을 작성하여라.
#예를 들어 a= [1, 4, 7, 2, 6, 8] 인 경우 반환값은 1+4-7+2-6+8=2이다. (오류??)

def alternatingSum(a):
    # 입력 리스트가 비어있으면 0 반환
    if not a:
        return 0

    # 각 항목에 대해 번갈아가며 +와 - 연산을 수행
    result = a[0]
    for i in range(1, len(a)):
        # 항목의 인덱스가 짝수이면 더하고, 홀수이면 뺌
        if i % 2 == 0:
            result += a[i]
        else:
            result -= a[i]

    return result

# 테스트
print(alternatingSum ([1, 4, 9, 16, 9, 7, 4, 9, 11 ]))    #-> -2
print(alternatingSum ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]))  # -> -5

#하나의 정수 n을 입려받아 n과 같은 크기의 삼각형 모양을 출력하는 프로그램 triangle1()을 작성하라. 예를 들어 triangle1(3)은 다음 그림(A)와 같다.

def triangle1(n):
    for i in range(1, n + 1):
        print('*' * i)

def triangle2(n):
    for i in range(1, n + 1):
        # 각 행에 필요한 공백 수 계산
        spaces = ' ' * (n - i)
        # 각 행을 형성하기 위해 공백과 '*' 문자를 연결
        stars = '*' * i
        # 행 출력
        print(spaces + stars)

def diamond(n):
    # 입력이 3 미만이거나 짝수인 경우 처리
    if n < 3 or n % 2 == 0:
        print("3 이상의 홀수를 입력해주세요.")
        return

    # 위쪽 부분 출력
    for i in range(1, n + 1, 2):
        spaces = ' ' * ((n - i) // 2)
        stars = '*' * i
        print(spaces + stars)

    # 아래쪽 부분 출력
    for i in range(n - 2, 0, -2):
        spaces = ' ' * ((n - i) // 2)
        stars = '*' * i
        print(spaces + stars)

triangle1(3)
triangle1(5)
triangle2(3)
triangle2(5)
diamond(5)
diamond(7)

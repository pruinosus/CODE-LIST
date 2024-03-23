#정수들의 리스트 a를 매개변수로 입 력 받아 각 항목들의 누적 값(accumulate)으로 이루어진 새로운 리스트를 만들어 반환하는 함수 accumulate()를 작성하여라. 
#즉, 반환값 b는 i 값이 0부터 len(a)-1까지 변하면서 각각의 b[i] =a[0] + a[1] + ... +a [i]의 값을 갖도록 한다

def accumulate(a):
    """
    주어진 리스트 a의 각 항목들을 누적하여 이루어진 새로운 리스트를 반환합니다.

    Parameters:
    - a (list): 정수들의 리스트

    Returns:
    - list: 각 항목들이 누적된 리스트
    """
    n = len(a)
    b = [None] * n

    # 첫 번째 항목은 그대로 누적 리스트에 복사
    b[0] = a[0]

    # 누적 값을 계산하여 리스트에 저장
    for i in range(1, n):
        b[i] = b[i-1] + a[i]

    return b

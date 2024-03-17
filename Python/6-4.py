#f(i,j) 가 다음과 같고,i와 j의 값이 0부터 99 사이의 정수라고 정의 될 
#f(i,j)의 최댓값을 구하는 함수 finaMax()를 파이썬으로 작성하여라,
#f(i,j) = (i^5+(2*(i^3)*(j^2))+(5i^2)+j+5000)mod10000 

def f(i, j):
    # 주어진 함수 f(i, j) = (i^5 + 2*(i^3)*(j^2) + 5*(i^2) + j + 5000) % 10000 계산
    return (i**5 + 2*(i**3)*(j**2) + 5*(i**2) + j + 5000) % 10000

def findMax():
    # 최댓값 및 해당하는 i, j를 저장할 변수 초기화
    max_value = 0
    max_i, max_j = 0, 0

    # i와 j가 0부터 99까지의 정수일 때의 모든 조합을 확인
    for i in range(100):
        for j in range(100):
            # 현재 조합에 대한 함수 값 계산
            current_value = f(i, j)
            
            # 현재 값이 최댓값보다 크면 최댓값 및 해당하는 i, j를 갱신
            if current_value > max_value:
                max_value = current_value
                max_i, max_j = i, j

    # 최댓값과 해당하는 i, j를 반환
    return max_value

# 최댓값을 찾아서 출력
print("최댓값:", findMax())    # 9997

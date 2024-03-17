#출생 연도를 입력받아 12간지의 띠를 반환하는 함수 chineseZodiac()를 작성하여라
def chineseZodiac(birth_year):
    """
    주어진 출생 연도에 대한 12가지 띠를 반환하고 바로 출력합니다.

    Parameters:
    - birth_year (int): 출생 연도
    """
    zodiac_animals = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
    
    # 출생 연도에 대한 띠 결정 (원숭이 띠로 가정)
    zodiac_index = (birth_year - 1900) % 12

    print(f"{birth_year} 년도는 {zodiac_animals[zodiac_index]} 띠 입니다.")

# 테스트
chineseZodiac(1968)

#연도를 나타내는 양의 정수 하나를 입력받아 해당 연도가 윤년인지 여부를 판단하는 함수 leapYear()를 작성하여라
#[힌트] 기본적으로 2월이 29일까지 존재하는 윤년(leap year)은 연도를 4로 나누어 떨어지는 경우, 즉 4의 베수인 경우에 한 번썩 돝아온다. 
#예를 들어 2020년과 2024년 은 윤년이고 2022, 2023년은 윤년이 아니다. 4의 배수이지만 연도의 끝자리가 00인 경우, 즉 100의 배수인 경우는 윤년이 아니다. 
#단, 400의 배수인 경우에는 운년이다. 그려므로 1600, 2000년은 윤년이지탄 1700, 1800, 1900, 2100, 그리고 2200년은 윤년이 아니다. 
#일단 가장 먼저 4로 나눠지지 않는 경우 False(운년이 아니므로)를 반환함으로써 경우의 수를 줄얼 수 있다
#▣ 자, 이제는 앞에서 정의한 leapYear()를 이용하여 연도와 월을 입력받아 해당 월의 마지막 일자를 반환하는 함수인 numDays()를 작성해 보자
#[힌트] 1,3,5,7,8,10,12월은 31일까지 있고 4, 6, 9, 11윌 30일까지 그리고 윤년이 아닌 2월은 28일까지, 윤년인 경우는 2월이 29일까지 있다

def leapYear(year):
    # 4로 나누어 떨어지면서
    # 100의 배수이지만 400의 배수인 경우 윤년
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def numDays(year, month):
    # 1, 3, 5, 7, 8, 10, 12월은 31일까지
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # 4, 6, 9, 11월은 30일까지
    elif month in [4, 6, 9, 11]:
        return 30
    # 2월은 윤년이면 29일, 아니면 28일
    elif month == 2:
        return 29 if leapYear(year) else 28
    # 그 외의 경우는 잘못된 입력으로 처리
    else:
        return "Invalid month"

# 동작확인
print(leapYear(2008), leapYear(2011), leapYear(2012))  # True False True
print(leapYear(2000), leapYear(2100), leapYear(2200))  # True False False
print(leapYear(2300), leapYear(2400), leapYear(3200))  # False True True

print("==============================================")

print(numDays(2000,1), numDays(2001,4), numDays(2004,8))  # 31 30 31
print(numDays(2004,9), numDays(2005,3), numDays(2005,7))  # 30 31 31
print(numDays(2008,2), numDays(2011,2), numDays(2012,2))  # 29 28 29
print(numDays(2000,2), numDays(2100,2), numDays(2200,2))  # 29 28 28
print(numDays(2300,2), numDays(2400,2), numDays(3200,2))  # 28 29 29

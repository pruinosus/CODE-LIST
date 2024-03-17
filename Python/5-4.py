#큰 병원에서 수혈을 위한 혈액 수급은 늘 중요한 문제다. 
#혈액형별로 필요한 혈액의 양과 준비된 혈액이 충분한지를 점검하는 함수 blood를 작성하여라. 
#입력되는 매개변수는 ABO 타입에 따라 준비된 혈액양인 supplyO, supplyA, supplyB, supplyAB와 각 헐액형 별 필요량 
#demandO, demandA, demandB, demandAB 등 8개의 정숫값이다. 
#문제를 간단하게 하기 위해서 Rh type은 고려하지 않고 ABO type만을 고러하기로 한다. 
#수헐이 가능한 경우에는 True를 반환하고 불가능한 경우에는 False를 반환한다.
  
#[힌트] 혈액을 수형할 수 있는 규칙은 다음과 같다.
#혈액형 0형은 0형만을 수헐받을 수 있다.
#혈액형 A형은 0, A형을 수헐받을 수 있다
#혈액형 B형은 0, B형을 수혈받을 수 있다
#혈액형 AB형은 네 가지 모든 혈액형을 수혈받을 수 있다



def blood(supplyO, supplyA, supplyB, supplyAB, demandO, demandA, demandB, demandAB):
    # 혈액형 0형은 0형만을 수혈받을 수 있다.
    if demandO > supplyO:
        return False
    
    # 혈액형 A형은 0, A형을 수혈받을 수 있다.
    if demandA > supplyO + supplyA:
        return False
    
    # 혈액형 B형은 0, B형을 수혈받을 수 있다.
    if demandB > supplyO + supplyB:
        return False
    
    # 혈액형 AB형은 네 가지 모든 혈액형을 수혈받을 수 있다.
    if demandAB > supplyO + supplyA + supplyB + supplyAB:
        return False

    # 모든 조건을 통과했으면 혈액 수혈 가능
    return True

# 동작확인
print(blood(50, 36, 11, 8, 45, 42, 10, 3))   # False
print(blood(50, 36, 11, 3, 45, 38, 10, 7))   # True

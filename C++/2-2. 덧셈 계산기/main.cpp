#include <iostream>

using namespace std;

//< >는 시스템 헤더 파일을 포함할 때 사용되고, ""는 사용자 정의 헤더 파일을 포함할 때 사용함
#include "Calculator.h"

int main(){
    //계산기 클래스 생성
    Calculator calc;
    //함수 실행
    calc.run();
}
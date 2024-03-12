#include <iostream>
using namespace std;

#include "Circle.h"

// 기본 생성자: 반지름을 기본값으로 초기화하고 원을 생성하는 생성자
Circle::Circle() {
    radius = 1; // 반지름을 기본값으로 초기화
    cout << "반지름" << radius; // 생성된 원의 반지름 출력
    cout << "원 생성" << endl; // "원 생성" 출력
}

// 매개변수를 받는 생성자: 매개변수로 받은 값을 반지름으로 설정하고 원을 생성하는 생성자
Circle::Circle(int r) {
    radius = r; // 매개변수로 받은 반지름으로 초기화
    cout << "반지름" << radius; // 생성된 원의 반지름 출력
    cout << "원 생성" << endl; // "원 생성" 출력
}

// 원의 면적을 계산하는 함수
double Circle::getArea() {
    return 3.14 * radius * radius; // 원의 면적 계산하여 반환
}

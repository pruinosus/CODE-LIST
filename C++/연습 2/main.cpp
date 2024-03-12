#include <iostream>
using namespace std;

#include "Circle.h"

int main() {
    Circle donut; // 반지름이 기본값인 원 객체 생성
    double area = donut.getArea(); // 원의 면적 계산
    cout << area << endl; // 원의 면적 출력
}
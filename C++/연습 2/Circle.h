#include <string>
#ifndef CIRCLE_H
#define CIRCLE_H

class Circle {
private:
    int radius; // 원의 반지름

public:
    Circle(); // 기본 생성자 선언
    Circle(int r); // 반지름을 인자로 받는 생성자 선언
    double getArea(); // 원의 면적을 계산하는 함수 선언
};

#endif
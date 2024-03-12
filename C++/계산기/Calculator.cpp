#include <iostream>
using namespace std;

#include "Calculator.h"
#include "Adder.h"

void Calculator::run() {
    Adder adder; // 기본 생성자를 호출하여 객체 생성
    cout << adder.process() << "\n"; // 객체의 process() 함수를 호출하고 결과 출력

    cout << "두 개의 수를 입력하세요: ";
    int a, b;
    cin >> a >> b;
    Adder adder2(a, b); // 매개변수를 받는 생성자를 호출하여 객체 생성
    cout << adder2.process()<<" 입니다."; // 객체의 process() 함수를 호출하고 결과 출력
}
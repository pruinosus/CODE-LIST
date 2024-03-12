#include <iostream>
#include "sadali.h"

using namespace std;

// sadali 클래스의 생성자 (매개변수 a와 b를 받아 윗변과 아랫변을 초기화)
sadali::sadali(int a, int b) {
    up = a;
    down = b;
    calculator_sadali(); // 사다리꼴의 넓이를 계산하는 함수 호출
}

// sadali 클래스의 생성자 (매개변수 a, b, c를 받아 윗변, 아랫변, 높이를 초기화)
sadali::sadali(int a, int b, int c) {
    up = a;
    down = b;
    hei = c;
    calculator_sadali(); // 사다리꼴의 넓이를 계산하는 함수 호출
}

// 사다리꼴의 넓이를 계산하는 멤버 함수
int sadali::calculator_sadali() {
    result = (((up + down) * hei) / 2); // 사다리꼴의 넓이를 계산하여 결과에 저장
    return result; // 계산된 넓이를 반환
}

// 사다리꼴 정보를 출력하는 멤버 함수
void sadali::print_sadali() {
    cout << "높이	: " << get_hei() << endl;    // 높이 출력
    cout << "윗변	: " << get_up() << endl;    // 윗변 출력
    cout << "아랫변	: " << get_down() << endl;    // 아랫변 출력
    cout << "결과	: " << get_result() << endl << endl; // 계산된 넓이 출력
}

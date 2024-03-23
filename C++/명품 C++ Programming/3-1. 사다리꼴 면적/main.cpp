#include <iostream>
#include "sadali.h"

using namespace std;

int main() {
    // 첫 번째 사다리꼴 객체 생성 및 초기화
    sadali sa3(10, 20, 30);
    sa3.print_sadali(); // 사다리꼴 정보 출력

    // 두 번째 사다리꼴 객체 생성 (기본 생성자를 사용하여 초기화)
    sadali sa2;
    sa2.print_sadali(); // 사다리꼴 정보 출력 (기본 생성자로 초기화되어 있으므로 모든 멤버 변수는 기본값으로 초기화됨)

    // 세 번째 사다리꼴 객체 생성 (각 멤버 변수를 개별적으로 설정하여 초기화)
    sadali sa1;
    sa1.set_up(10); // 윗변 설정
    sa1.set_down(30); // 아랫변 설정
    sa1.set_hei(20); // 높이 설정
    sa1.print_sadali(); // 사다리꼴 정보 출력

    return 0;
}

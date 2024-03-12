#define _CRT_SECURE_NO_WARNINGS // strcpy 함수를 사용하기 위해 선언된 매크로입니다.

#include <iostream> // 표준 입출력 스트림 라이브러리를 포함합니다.
#include <cstring> // C 스타일 문자열 처리 함수를 포함합니다.
#include "Car.h" // Car 클래스의 선언이 있는 헤더 파일을 포함합니다.

using namespace std; // 표준 네임스페이스를 사용합니다.
using namespace CAR_CONST; // CAR_CONST 네임스페이스를 사용합니다.

// 주어진 ID와 연료 수준으로 자동차를 초기화합니다.
// const char* 형식으로 선언함, 문자열 리터럴과 같이 수정할 수 없는 상수 문자열을 받기 위해서입니다.
void Car::InitMembers(const char* ID, int fuel) {
    strcpy(gamerID, ID); // ID를 gamerID 멤버 변수에 복사합니다.
    fuelGauge = fuel; // 연료 수준을 설정합니다.
}

// 자동차의 현재 상태를 ID, 연료 수준 및 속도로 표시합니다.
void Car::ShowCarState() {
    cout << "소유자ID    : " << gamerID << endl; // 소유자 ID를 출력합니다.
    cout << "연료량      : " << fuelGauge << endl; // 연료량을 출력합니다.
    cout << "현재속도    : " << curSpeed << endl; // 현재 속도를 출력합니다.
}

// 자동차의 속도를 증가시켜 가속합니다.
void Car::Accel() {
    // 연료가 남아있는지 확인하여 가속 가능 여부를 판단합니다.
    if (fuelGauge <= 0) {
        // 연료가 부족하여 가속할 수 없습니다. 함수를 종료합니다.
        return;
    }
    else {
        // 연료를 소모하고 속도를 증가시킵니다.
        fuelGauge -= FUEL_STEP;
    }

    // 현재 속도와 가속 단계를 더한 값이 최대 속도를 초과하는지 확인합니다.
    if ((curSpeed + ACC_STEP) >= MAX_SPD) {
        // 최대 속도를 초과하는 경우 최대 속도로 설정합니다.
        curSpeed = MAX_SPD;
    }
    else {
        // 최대 속도를 초과하지 않는 경우 속도를 증가시킵니다.
        curSpeed += ACC_STEP;
    }
}

// 자동차의 속도를 감소시켜 감속합니다.
void Car::Break() {
    // 현재 속도가 제동 속도보다 작은지 확인합니다.
    if (curSpeed <= BRK_STEP) {
        // 더이상 제동할 속도가 없습니다. 속도를 0으로 설정합니다.
        curSpeed = 0;
        return;
    }
    else {
        // 제동 속도 만큼 속도를 감소시킵니다.
        curSpeed -= BRK_STEP;
    }
}

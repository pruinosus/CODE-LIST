#pragma once

// CAR_CONST 네임스페이스에는 자동차 속성과 관련된 상수 포함
namespace CAR_CONST {
    // 자동차 속성에 대한 상수들 (열거형)
    enum {
        ID_LEN = 20,        // 게이머 ID의 최대 길이
        MAX_SPD = 200,      // 자동차의 최대 속도
        FUEL_STEP = 2,      // 연료 소모 단계
        ACC_STEP = 10,      // 가속 단계
        BRK_STEP = 10       // 제동 단계
    };
}

// Car 클래스는 특정 속성과 기능을 갖춘 기본 자동차를 나타냅니다.
class Car {
private:
    char gamerID[20];    // 자동차의 게이머 ID를 저장하는 배열
    int fuelGauge;       // 자동차의 연료 수준을 나타내는 정수
    int curSpeed = 0;    // 자동차의 현재 속도를 나타내는 정수

public:
    // 주어진 ID와 연료 수준으로 자동차를 초기화합니다.
    // ID: 자동차의 소유자 ID를 나타내는 문자열입니다. 
    //     const char* 형식으로 선언되었습니다. 이는 문자열 리터럴과 같이 수정할 수 없는 
    //     상수 문자열을 받기 위함입니다.
    // fuel: 자동차의 초기 연료 수준을 나타내는 정수입니다.
    // 반환값: 없음
    void InitMembers(const char* ID, int fuel);

    // 자동차의 현재 상태를 ID, 연료 수준 및 속도로 표시합니다.
    // 반환값: 없음
    void ShowCarState();

    // 자동차의 속도를 증가시켜 가속합니다.
    // 반환값: 없음
    void Accel();

    // 자동차의 속도를 감소시켜 감속합니다.
    // 반환값: 없음
    void Break();
};

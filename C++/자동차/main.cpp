#include "Car.h" // Car 클래스의 선언이 있는 헤더 파일을 포함합니다.

int main() {
    Car pruinosus; // Car 클래스의 객체를 생성합니다.

    // Car 객체의 멤버 함수들을 호출하여 자동차의 상태를 초기화하고 표시합니다.
    pruinosus.InitMembers("pruinosus", 100); // "pruinosus"라는 소유자 ID와 연료량 100으로 초기화합니다.
    pruinosus.ShowCarState(); // 자동차의 현재 상태를 출력합니다.

    // 자동차의 속도를 증가시키고 감속합니다.
    pruinosus.Accel(); // 가속을 수행합니다.
    pruinosus.Break(); // 감속을 수행합니다.
}

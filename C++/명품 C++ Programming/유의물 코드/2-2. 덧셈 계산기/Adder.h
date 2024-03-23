#ifndef ADDER_H // 만약 ADDER_H 매크로가 정의되어 있지 않다면 아래 코드를 실행합니다.
#define ADDER_H // ADDER_H 매크로를 정의합니다.

using namespace std; //std::의 접두사를 제외하고 사용가능

//클래스 선언
class Adder {
private:
    int option_1, option_2; // 기본값으로 초기화된 옵션 변수

public:
    //덧셈 파일의 함수부분이 짧아 클래스 내부에서 선언
    inline Adder() : option_1(5), option_2(10) {} // 기본 생성자를 명시적으로 선언하고, 이를 디폴트로 지정함
    inline Adder(int a, int b) : option_1(a), option_2(b) {} // 매개변수를 받는 생성자
    inline int process() { return option_1 + option_2; } // 덧셈을 수행하는 함수
};

#endif
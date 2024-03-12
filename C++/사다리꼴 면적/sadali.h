#pragma once

class sadali {
private:
    // 사다리꼴의 윗변, 아랫변, 높이, 넓이를 나타내는 멤버 변수들
    int up = 10, down = 10, hei = 10, result = (up + down) * hei / 2;

public:
    // 매개변수 없는 기본 생성자
    sadali() = default;

    // 매개변수 있는 생성자 함수
    sadali(int a, int b);
    sadali(int a, int b, int c);

    // 윗변을 반환하는 함수
    inline int get_up() { return up; };

    // 아랫변을 반환하는 함수
    inline int get_down() { return down; };

    // 높이를 반환하는 함수
    inline int get_hei() { return hei; };

    // 넓이를 반환하는 함수
    inline int get_result() { return result; };

    // 변수 값 수정 및 사다리꼴 넓이 재계산
    inline void set_up(int up2) { up = up2; calculator_sadali(); };
    inline void set_down(int down2) { down = down2; calculator_sadali(); };
    inline void set_hei(int hei2) { hei = hei2; calculator_sadali(); };
    inline void set_result(int result2) { result = result2; };

    // 사다리꼴의 넓이를 계산하는 함수
    int calculator_sadali();

    // 사다리꼴 정보를 출력하는 함수
    void print_sadali();
};

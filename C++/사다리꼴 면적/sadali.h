#ifndef SADALI_H
#define SADALI_H

class sadali{
    private:
        int up, down, hei, result;
    public:
        //생성자
        sadali();
        sadali(int a,int b);
        sadali(int a,int b,int c);
        
        //현제 값 추출
        inline int get_up(){ return up; };
        inline int get_down(){ return down; };
        inline int get_hei(){ return hei; };
        inline int get_result(){return result; };

        //변수 값 수정
        inline int set_up(int up2){ up = up2; };
        inline int set_down(int down2){ down = down2; };
        inline int set_hei(int hei2){ hei = hei2; };
        inline int set_result(int result2){ result = result2 };

};

#endif
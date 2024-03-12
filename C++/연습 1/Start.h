#include <string>
#ifndef START_H


#define START_H




class Start

{

    string name;

    short HP;


public:

    Start();

    Start(string name, short HP);

    void info();

    void set_info(string name, short HP);

};




#endif
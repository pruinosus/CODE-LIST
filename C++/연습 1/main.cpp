#include <iostream>


using namespace std;


#include "Start.h"





Start::Start(){} 

Start::Start(string name, short HP) 

{

    this->name = name;

    this->HP = HP;

}




void Start::info()

{

    cout << "--------------------" << endl;

    cout << "name: " << this->name << endl;

    cout << "HP: " << this->HP << endl;

}




void Start::set_info(string name, short HP)

{

    this->name = name;

    this->HP = HP;

}
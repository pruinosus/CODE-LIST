#include <iostream>


using namespace std;


#include "Start.h"



int main()

{

    Start Tracer("Tracer", 150), Pharah("Pharah", 200), Mercy;

    Pharah.info();



    Mercy.set_info("Mercy", 200);

    Mercy.info();

}



class mytclass {

    public : 

    int value ; 

    void  setter_value() ; 

    mytclass (int y ) {

        value = y ; 
    }

} ; 



class veicule: mytclass {

    public:

    char myname ; 

    veicule() :myname() {


    }

} ;

enum value {
    midle , 
    hight , 
    biggest 
}  ; 





int main() {

    int value = 0 ;   

    try {

        int age = 18 ; 

        if (age >=  18) {
            

        }  else {

            throw (age)  ; 
        }
    }
    catch (value) {


    }
    mytclass obj(10) ;








    return 0 ; 
}
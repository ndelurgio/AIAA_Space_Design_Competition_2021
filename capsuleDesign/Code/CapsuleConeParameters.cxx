//Author: Pete Lealiiee Jr, University of Texas: Aerospace Engineering 
#include <iostream>
#include <math.h> 

#define PI 3.14159265358979323846

class param{
    private:
        double ha, theta, f, r;
        int type;
    public:
        param(){
            do{
                std::cout << "Allowable Height [uL]:";
                std::cin >> ha;
                std::endl(std::cout);
            }while(ha<=0);

            do{
                std::cout << "Input Type:" << std::endl;
                std::cout << "0: Input Theta (Convergence Angle) [degrees]" << std::endl;
                std:: cout << "1: Input f (Radial Fraction containing Max Height)" << std::endl;
                std::cout << " Type:";
                std::cin >> type;
                std::endl(std::cout);
            }while(type != 1 && type !=0 );

            switch (type){
                case 0:
                    std::cout << " Theta[degrees]:";
                    std::cin >> theta;
                    theta = (theta/180)*PI;
                    std::endl(std::cout);
                    break;
                case 1:
                    std::cout << " f:";
                    std::cin >> f;
                    std::endl(std::cout);
                    break;
                default:
                    throw("Invalid Type: Choose 0 or 1");
                    break;
            }
        }

        void set_r(double ri){
            r = ri;
            return;
        }

        double get_ha(){
            return ha;
        };

        double get_type(){
            return type;
        };

        double taneq(){
            switch (type){
                case 0:
                    return tan(theta);
                    break;
                case 1:
                    return ha/(r*(1-f));
                    break;    
                default:
                    throw("Invalid Type: Choose 0 or 1");
                    return -1;
                    break;
            }
        };

        void solve_secondary(){
            switch (type){
                case 0:
                    f = 1 - (ha/(r*taneq()));
                    break;
                case 1:
                    theta = atan(taneq());
                    break;    
                default:
                    throw("Invalid Type: Choose 0 or 1");
                    break;
            }
        };

        void print_param(){
            solve_secondary();
            std::cout << "Allowable height [uL]: " << ha << std::endl;
            std::cout << "Smaller Radius [uL]: " << f*r << std::endl;
            std::cout << "Larger Radius [uL]: " << r << std::endl;
            std::cout << "Radial Fraction: " << f << std::endl;
            std::cout << "Convergence Angle (theta) [Degrees]: " << theta*180/PI << std::endl;
        };  

};


double SolvePartialCone(double ri, param param1, double Vexp){
    param1.set_r(ri);
    double ha = param1.get_ha();
    double taneqi = param1.taneq(); 
    double V = (PI*ha/3) * ( (3*(pow(ri,2))) - (3*ha*ri/taneqi) + (pow(ha,2)/pow(taneqi,2))) ;
    return(V-Vexp);
};


void find_zero( param& param1, double Vexp, double h = 0.001){
    double rxint = 5.0;
    double rx = rxint;
    param1.set_r(rx);
    // Newton Method
    while ( abs( SolvePartialCone(rx,param1,Vexp) ) > 1.e-10 ) {
        double g = ( SolvePartialCone(rx+h,param1,Vexp)-SolvePartialCone(rx,param1,Vexp) )/h;
        rx = rx - (SolvePartialCone(rx,param1,Vexp)/g);
        if(rx<0){rxint = rxint*1.5; rx = rxint;} //Throw the initial condition out further if solution approches negative solution
        param1.set_r(rx);
    };
    return;
};


int main(){
    double Vexp;
    do{
        std::endl(std::cout);
        std::cout << "Expected Volume [uL^3]:";
        std::cin >> Vexp;
        std::endl(std::cout);
    }while(Vexp<=0);

    param parami;

    find_zero( parami, Vexp);

    parami.print_param();
    std::endl(std::cout);

    return 0;
}



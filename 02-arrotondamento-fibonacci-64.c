#include<stdio.h>
#include <math.h>

int main()
{
    double z1 = (1+sqrt(5))/2;
    double z2 = (1-sqrt(5))/2;
    printf("z1 %5.50f\n", z1);
    printf("z2 %5.50f\n", z2);
        
    double C[2][2];
    C[0][0] = 1;
    C[0][1] = 1;
    C[1][0] = z1;
    C[1][1] = z2;
    
    double Cinv[2][2];
    Cinv[0][0] = -z2/(z1-z2);
    Cinv[0][1] = 1/(z1-z2);
    Cinv[1][0] = -z1/(z2-z1);
    Cinv[1][1] = 1/(z2-z1);
    
    double Cres[2][2];
    
    Cres[0][0] = Cinv[0][0]*C[0][0] + Cinv[0][1]*C[1][0];
    Cres[0][1] = Cinv[0][0]*C[0][1] + Cinv[0][1]*C[1][1];
    Cres[1][0] = Cinv[1][0]*C[0][0] + Cinv[1][1]*C[1][0];
    Cres[1][1] = Cinv[1][0]*C[0][1] + Cinv[1][1]*C[1][1];
    
    printf("Cres[0][0] %5.50f\n", Cres[0][0]);
    printf("Cres[0][1] %5.50f\n", Cres[0][1]);
    printf("Cres[1][0] %5.50f\n", Cres[1][0]);
    printf("Cres[1][1] %5.50f\n", Cres[1][1]);
       
    return 0;
}

/* 
 * File:   countmultip.c
 * Author: Nemo(Mohammad Mirian)
 *
 * Created on August 14, 2018, 2:12 PM
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
    int Num;
    
    printf("Enter a number from 1 to 25: ");
    scanf("%d",&Num);
    
    for (int i=1;i<=Num;i++)
    {
        printf("%3d x 7 = %4d\n",i,i*7);
    }
    return (EXIT_SUCCESS);
}


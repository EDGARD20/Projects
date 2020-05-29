/* 
 * File:   main.c
 * Author: Nemo(Mohammad Mirian)
 *
 * Created on August 20, 2018, 1:23 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    srand((unsigned int)time(NULL));
    /*The srand(x) function sets the seed of the random number 
     * generator algorithm used by the function rand( ). 
     * A seed value of 1 is the default setting yielding 
     * the same sequence of values as if srand(x) were not used. 
     * Any other value for the seed produces a different sequence. 
     * srand(time(NULL));
     */
    float a = 35.0, TempList[7];
    for (int i=1;i<8;i++)
    {
        TempList[i]=(((float)rand()/(float)(RAND_MAX)) * a);
        printf("Day %2d : %5.2f\n",i,TempList[i]);
    }
    
    return 0;
}


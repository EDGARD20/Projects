/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   magicFunction.c
 * Author: Nemor(Mohammad Mirian)
 *
 * Created on August 13, 2018, 12:54 PM
 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void magicFunction(int value); // Introducing the magicFunction
                               /* All Function used in C/C++ should introduce 
                                here.*/

int main (int argc, char *argv[]) // main function
{
    int value;
    if(argc < 2)
    {
        printf("%d",argc);
        printf("Too few arguments: <program> <value>\n");
        exit(1);
    }  
        
    value = atoi(); /* The C library function int "atoi" converts
                            *  the string argument to an integer. 
                            */    
    printf(value);
    magicFunction(value);   // calling function  
    return 0;
}
/*This magicFunction is to calculate and display the smallest of odd and even 
 *  numbers of "Value" which their multiplication is equal to the "value"
 */
void magicFunction(int value)
{
    int i, count = 1; // Defining variable i & count.
    int n = value; //Value will store in n as an integer number
    
    while (n%2 == 0)
    {
        printf("%i: %d\n",count++, 2);
        n = n/2;
    }
    
    //sqrt is a function that calculates the square root of a value
    for (i=3; i<=sqrt(n); i=2+i)
        /* i start from 3 until i reach square root of n
         * in each iteration i is always an odd number
         */
    {
        while (n%i == 0) /* while the remainder of n by i is 0 then
                          * adds a number to the previous count value and then 
                          * print the new count value and i
                          */ 
        {
            printf("%i: %d\n",count++, i);
            n = n/i; /* If the Condition passed then n is equal to previous n
                      * divided by i
                      */
        }
    }
 
    if (n > 2)
    {
        printf ("%i: %d\n",count++, n);
        /*
         * %i      => Is stand for integer, used for print in integer 
         *              numbers which here used for printing the value of count.
         * %d      => Is stand for decimal, used for print in decimal 
         *              numbers which here used for printing the value of n.
         * count++ => Adds a number to the previous count value.
         */
    }
}


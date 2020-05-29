/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: Nemo(Mohammad Mirian)
 *
 * Created on August 11, 2018, 6:16 PM
 */

#include <stdio.h>
#include <stdlib.h>
int main() {
    char name[255], ch;
    int i = 0, j=1,k=0;
    printf("Enter name between 1 & 255 characters: ");
    while(ch != '\n')    // terminates if user hit enter
    {
        ch = getchar();
        name[i] = ch;
        i++;
    }
    name[i] = '\0';       // inserting null character at end
    printf("Name: %s", name);
    while(name[j]!='\0')
    {
        if ((k==10) || (k==0))
        {  printf("|");
            k=1;
        }
        else if ((k<=4) || ((k>5)&&(k<=9)))
        {
            printf("-");
            k++;
        }
        else if ((k==5))
        {  printf("+");
            k++;  
        }
        j++;
    }
    return 0;
}


// Counting numbers
/*
 int main() {
    int S,k=0;
    printf("Please Input a number between 1 & 255:\t");
    scanf("%d",&S);
    printf("The number is = %d \n",S);
    for (int i=1;i<=S;i++)
    {
        if ((k==10) || (k==0))
        {  printf("|");
            k=1;
        }
        else if ((k<=4) || ((k>5)&&(k<=9)))
        {
            printf("-");
            k++;
        }
        else if (k==5)
        {  printf("+");
            k++;
        }         
    }
    return 0;
}
 */
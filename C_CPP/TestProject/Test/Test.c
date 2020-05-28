/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   STD_Calculator.c
 * Author: moham
 *
 * Created on August 26, 2018, 12:38 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
 * 
 */

int val,i=0,Arr[1],temp[1];
float sum=0,mu=0,Mean,sumIn=0.0,Squre=0.0;

float Getmean(int max);
void GetArray(int max);
float SquareRoot(int max,int Mu);


int main() {
        printf("How many value do you have: ");
    scanf("%d",&val);
    
    int Arr[val],temp[val];
    int MAX=val-1;
    
    
    GetArray(MAX);
    Getmean(MAX);
    
        printf("mu = %f",mu);
        
    SquareRoot(MAX,mu);
    
        printf("\n\nSTD = %f",Squre);
    
    return (EXIT_SUCCESS);
}




void GetArray(int max){
     printf("Enter You value:\n");
    int k=0,num;
    while (k <= max){
        printf("%d th: ",k+1);
        scanf("%d",&num);
        Arr[k]=num;
        k++;
    }
}


float Getmean(int max){
    int j=0;

    while(j <= max)
    {
        sum +=Arr[j];
        j++;
    }
    mu=sum/(max+1);
    return mu;
}

float SquareRoot(int max,int Mu){
    int i=0;
    while (i <= max){
        
        sumIn += pow((Arr[i] - Mu), 2);
        i++;
    }
    Squre = sqrt(sumIn/max);
    printf("\n\nSTD = %f",Squre);
    return Squre;
}
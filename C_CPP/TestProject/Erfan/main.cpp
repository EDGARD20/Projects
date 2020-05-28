/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: a318925
 *
 * Created on den 19 Februari 2020, 09:21
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int operationCases(char opr){
    if(opr == '+'){
        return 1;
    }
    else if(opr == '*'){
        return 2;
    }
    else if(opr == '-'){
        return 3;
    }
    else if(opr == '/'){
        return 4;
    }
    else if(opr == 'm'){
        return 5;
    }
    else if(opr == 's'){
        return 6;
    }
    else if(opr == '='){
    }
    else{
        return 7;
    }
}

void discription(){
    cout <<"\n\n------------------------------توضیحات------------------------------\n"
            "برای استفاده از ماشین حساب از روش زیر استفاده کنید\t\t  \n"
            "ابتدا یک عدد را وارد کنید سپس عملگر مورد نظر را زده و به همین ترتیب\n"
            "ادامه دهید\t\t\t\t\t\t\t \n"
            "برای مشاهده جواب در بخش عملگرها از = استفاده کنید \t\t \n "
            "===================================================================\n"
            "\t   m در بخش عملگر برای محاسبه محیط یک دایره دکمه \n"
            "\t\t  s و برای محاسبه مساحت  حرف \n"
            "را وارد کرده و جواب را دریافت و یا به ادامه محاسبه بپردازید      \n"
            "------------------------------------------------------------------\n\n";
}


float mohitJesm(float num1){
    cout<< "\n شیع مورد نظر کدام است: \n\n"
            "1. مربع \n"
            "2. مستطیل \n"
            "3. مثلت  - مثلث متساوی الاضلاع - مثلث متساوی الساقین  \n"
            "4. دایره \n"
            "5. لوزی\n\n\n"
            "انتخواب شما :  ";
    int a;
    float num2,num3;
    cin >> a;
    if (a == 1)
        return num1*4;
    else if (a == 2){
        cout << "ضلع دوم را وارد کنید: ";
        cin >> num2;
        return (num1 + num2)*2;
    }
    else if (a == 3){
        cout << "ضلع دوم را وارد کنید: ";
        cin >> num2;
        cout << "ضلع سوم را وارد کنید: ";
        cin >> num3;
        return num1+num2+num3;
    }
    else if (a == 4)
        return num1 * 3.14;
    else if (a == 5)
        return num1 * 4;
}

void calculator(){
    char opr;
    int num,numTemp,sum,returnedOpr,count=0;
    int oprCnt= 0;
    float mohit,masahat;
    do{
        if (oprCnt == 0){
            cout << "عدد را وارد کنید: ";
            cin >> num;
            oprCnt++;
            cout << "عملگر: ";
            cin >> opr;
            }
        else {
            cout << "عملگر: ";
            cin >> opr;
            }
        returnedOpr=operationCases(opr);
        switch(returnedOpr){
            case 1:{ // jam
                if (count == 0){
                    cout << "عدد را وارد کنید: ";
                    cin >> numTemp;
                    sum = num + numTemp;
                    count++;
                }
                else {
                    cout << "عدد را وارد کنید: ";
                    cin >> num;
                    sum = sum + num;
                }
                break;
            }
            case 2:{ // zarb
                if (count == 0){
                    cout << "عدد را وارد کنید: ";
                    cin >> numTemp;
                    sum = num * numTemp;
                    count++;
                }
                else {
                    cout << "عدد را وارد کنید: ";
                    cin >> num;
                    sum = sum * num;
                }
                
                break;
            }
            case 3:{ // tafrig
                    if (count == 0){
                        cout << "عدد را وارد کنید: ";
                        cin >> numTemp;
                        sum = num - numTemp;
                        count++;
                }
                else {
                    cout << "عدد را وارد کنید: ";
                    cin >> num;
                    sum = sum - num;
                }
                
                break;
            }
            case 4:{ // tagsim
                    if (count == 0){
                        cout << "عدد را وارد کنید: ";
                        cin >> numTemp;
                        sum = num / numTemp;
                        count++;
                }
                else {
                    cout << "عدد را وارد کنید: ";
                    cin >> num;
                    sum = sum / num;
                }
                break;
            }
            
            case 5:{ // Mohit Ashya
                if (count == 0){
                    sum = mohitJesm(num);
                    cout <<"محیط = \n" << sum ;
                    count++;
                }
                else{
                    cout << "حاصل محاسبه تاکنون = \n" << sum;
                    cout <<" ایا ازاین حاصل به عنوان عدد اول خود استفاده میکنید؟ \n"
                            "1. بله \n"
                            "2. خیر  \n";
                    int yesno;
                    cin >> yesno; 
                    
                    if(yesno == 1){
                        sum = mohitJesm(sum);
                       
                    }
                    else if (yesno == 2){
                        cout << "ظلع را وارد کنید: ";
                        cin >> num;
                        sum = mohitJesm(num);
                    }
                    
                }
                break;
            }
            case 6:{ // masahat

                break;
            }
            
            case 7:{ 
                cout << "عملگر اشتباه است لطفا مجدد تکرار کنید  \n\n";
                opr = '=';
                break;
            }
                
        }
        
        
    }while(opr != '=');
    cout << "جواب میشود =    \n"<<sum;
}


int main(int argc, char** argv) {

    discription();
    calculator();
    
    return 0; 
}
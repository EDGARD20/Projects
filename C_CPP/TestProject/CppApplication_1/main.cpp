
/* 
 * File:   TestCalculator.cpp
 * Author: Administrator
 *
 * Created on December 22, 2019, 6:49 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;


int introduction(){
    cout <<"\n\n\nThis is my calculator:"
            "\nchoose a number to continue:"
            "\n1= jam"
            "\n2 = tafrig"
            "\n3 = zarb"
            "\n4 = tagsim"
            "\n5 = Masahat"
            "\n6 = Mohit"
            "\n0 = Exit"
            "\n your choice: ";
    int x;
    cin >> x;
    return x;
}



int main(int argc, char** argv) {
    int n=0, sum,num;
    char ch;
    do{
        n= introduction();
        switch(n){
            case 1:{
                while(1){
                    cout<<"Adad ra vared konid: ";
                    cin>>ch;
                    if(ch !='='){
                        num = int(ch) - 48;
                        if(0<num<9)
                        sum += num;
                    }
                    else{   
                        cout<<"sum= "<<sum;
                        break;
                    }
                }
                break;
            }
            case 2:{
                while(1){
                    cout<<"Adad ra vared konid: ";
                    cin>>ch;
                    if(ch !='='){
                        num = int(ch) - 48;
                        if(0<num<9)
                        sum -= num;
                    }
                    else{   
                        cout<<"sum= "<<sum;
                        break;
                    }
                }
            }
        }
        
    }while(n != 0 );
    
    return 0;
}


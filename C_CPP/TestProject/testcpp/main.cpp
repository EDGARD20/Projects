/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Nemo
 *
 * Created on February 18, 2020, 7:45 PM
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    char n;
    cin >> n;
    if (n == '=')
        cout << "hi";
    else{
        cout << n + n /4;
    }
    return 0;
}


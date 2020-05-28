
/* 
 * File:   main.c
 * Author: Nemo
 *
 * Created on January 1, 2020, 6:14 PM
 */

#include <stdio.h>
#include <stdlib.h>



// Implement a struct for putting all the input into a stack

struct phonebook{
    int number; // the number of contact that user may input
    char name[25]; // 25 character for name and family should be enough
    char address[45];//45 char for address should be enough
    char PoBox[15]; // it will use for PoBox number or ID number, you can also
                    // use another one just for ID, or any information you wanna 
                    // add
    struct phonebook* next; // push the pointer to next room 
};

// implement the head of stack
struct phonebook* head; // it will use the next pointer as the head of pointer



//recall all the function here

// insert function
void insert_phonebook(int num);
// edit function
void edit_phonebook(int num, int PartNumber);
// display function
void print_phonebook(int call);

// some Global variable

int choice, j=0,i = 1,Count = 1, EditNumber = 0,partNumber;

int main(int argc, char** argv) {

    // start to build the main function first to see what function we may need
    // first set head as null
    head = NULL;

    printf("---- Phone Book---- \n");
    printf("--------------------\n\n");
    do{
       printf("\n\n\t Choose Your Wish:\n");
       printf("\t---------------------------\n");
       printf("\t1. Enter\n\t2. Display\n\t3. Edit\n\t4. Exit\n\n\n\t->: ");
       scanf("%d",&choice);
       
       // Switch between the choices
       
       switch(choice){
           case 1:{
               insert_phonebook(i);
               i++;
               break;
           }
           case 2:{
               print_phonebook(i);
               break;
           }
           case 3:{
               do{
                    //asking user what part of the phone book needs to change
                    printf("Enter your choice to modify: \n"
                            "---------------------------------------\n");
                    printf("\t1. Name\n\t2. Address\n\t3. PoBox/ID\n\t4. All\n\t5. Back\n\n");
                    scanf("%d", &EditNumber);
                    switch(EditNumber){
                        case 1:{
                            printf("Which contact number you want to modify: \n");
                            scanf("%d",&partNumber);
                            edit_phonebook(1, partNumber);
                            break;
                        }
                        case 2:{
                            printf("Which contact number you want to modify: \n");
                            scanf("%d",&partNumber);
                            edit_phonebook(2, partNumber);
                            break;
                        }
                        case 3:{
                            printf("Which contact number you want to modify: \n");
                            scanf("%d",&partNumber);
                            edit_phonebook(3, partNumber);
                            break;
                        }
                        case 4:{
                            printf("Which contact number you want to modify: \n");
                            scanf("%d",&partNumber);
                            edit_phonebook(4, partNumber);
                            break;
                        }
                    }
                    
                }while(EditNumber != 5);
                break;
           }
       }
        
    }while(choice != 4);
    
    
    
    return (EXIT_SUCCESS);
}



void insert_phonebook(int num){
   // we need a memory here
    struct phonebook *userInsert = (struct phonebook*)malloc(sizeof (struct phonebook));
    userInsert->number = num;
    
    //runs only once
    if(j == 0){
        printf("\n\n+------------------------------HINT--------------------------------+\n");
        printf("|  Name:       David,Jonson                                        |\n"
               "|  Address:    Sruvaregatan-22.CityName,CountryName,ApartmentNo    |\n"
               "|  PoBox/ID:   30432/19998832344                                   |\n"
               "|------------------------------------------------------------------|\n"
               "|\t\t No white space is acceptable \t\t\t   |\n"
               "+------------------------------------------------------------------+\n\n");
        j++;
    }
    
    printf("Enter First and Last name:   ");
    scanf("%s",&(userInsert->name));
    
    printf("Enter address:   ");
    scanf("%s", &(userInsert->address));
    
    printf("Enter PoBox/ID no.:   ");
    scanf("%s",&(userInsert->PoBox));
    
    // sort out the list by input, The first entry stay at the top of the list
    if(head == NULL){
        head = userInsert;
        userInsert->next = NULL;
    }
    else{
        struct phonebook *temp =head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = userInsert;
        userInsert->next = NULL;
    }
}



// Display phone book, display all existing items in a list 
void print_phonebook(int call){
    // read the contact number to display.
    // implement new temporary struct to put all the existing item inside and print it out 
    struct phonebook* temp = head;
    printf("Contact List:\n\n ");
    while(temp != NULL){
        printf(" No:  %d\nName: \t%s\nAddress: \t%s\nPoBox/IDno: \t%s\n\n",
                Count, temp->name, temp->address,temp->PoBox);
        temp = temp->next;
        Count++;
    }
    printf("\n");
}


void edit_phonebook(int num, int PartNumber){
    //implement a new struct for searching contact number;
    struct phonebook* temp=(struct phonebook*)malloc(sizeof (struct phonebook));
    temp = head;
    // Searching for the contact number that user is looking for
    while(temp->number != PartNumber){
        temp = temp->next;
    }
    
    
    if( num == 1){
        printf(" Enter the new name and family name: \n\t");
        scanf("%s",&(temp->name));
    }
    else if (num == 2){
        printf(" Enter the new address: \n\t");
        scanf("%s",&(temp->address));
        
    }
    else if (num == 3){
        printf(" Enter the new PoBox/IDno: \n\t");
        scanf("%s",&(temp->PoBox));
        
    }
    else if( num ==4){
        printf(" Enter the new name and family name: \n\t");
        scanf("%s",&(temp->name));
        
        printf(" Enter the new address: \n\t");
        scanf("%s",&(temp->address));
        
        printf(" Enter the new PoBox/IDno: \n\t");
        scanf("%s",&(temp->PoBox));
    }
    Count =1;
    
}
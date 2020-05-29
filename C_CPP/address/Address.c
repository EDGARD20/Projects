/* 
 * File:   Address.c
 * Author: Nemo(Mohammad Mirian)
 *
 * Created on August 21, 2018, 3:10 PM
 */



#include <stdio.h>
#include <stdlib.h>
struct User
{
    int number;
    char name[25];
    char address[25];
    char PoBox[25];
    struct User* next;
};

struct User* head;

void print_user(int Call);
void Change(int Num,int Pnum);
void insert_user(int num);

int choice,i=1,chg=1,PN,j=0,value,Count=1;
char NewName;

int main()
{
    head = NULL;

    printf("  ..Contact Book..\n");
    printf("-----------------------------");
    
    do{
        printf("\n\n\tChoose Your wish\n");
        printf("-----------------------------");
        printf("\n     1. Push\n     2. Display\n     3. Edit\n     4. Exit\n");
        printf("\n  Enter your choice: ");
        scanf("%d", &choice);

        switch(choice){
            case 1:{
                insert_user(i);
                i++;
                break;}
            
            case 2:{
                print_user(i);
                break;}
            
            case 3:{
                do{
                    printf("Enter your Choice:");
                    printf("\n------------------------------\n");
                    printf("     1: Name\n     2: Address\n     3: PoBox/P-number\n     4: All\n     5: Break\n\t:");
                    scanf("%d",&chg);

                switch(chg){
                    case 1:{
                        printf("Which Contact you want to Edit:\t");
                        scanf("%d",&PN);
                        Change(1,PN);
                        break;
                    }
                    case 2:{
                        printf("Which Contact you want to Edit:\t");
                        scanf("%d",&PN);
                        Change(2,PN);
                        break;
                    }
                    case 3:{
                        printf("Which Contact you want to Edit:\t");
                        scanf("%d",&PN);
                        Change(3,PN);
                        break;
                    }
                    case 4:{
                        printf("Which Contact you want to Edit:\t");
                        scanf("%d",&PN);
                        Change(4,PN);
                        break;
                    }
                }
                }while(chg != 5);
            }
        }
    }while(choice != 4);
    return 0;
}

void print_user(int Call){
    struct User* temp = head;
    while(temp != NULL)
    {
        printf("\nContact No.%d\nName:\t\t%s \nAddress:\t%s \nPoBox/P-number: %s\n",Count, temp -> name, temp-> address, temp->PoBox);
        temp = temp->next;
        Count++;
    }
    printf("\n");
}

void Change(int Num,int Pnum){
    struct User *temp = (struct User*)malloc(sizeof(struct User));
    temp = head;
    
    while(temp->number != Pnum){
        temp = temp->next;
    }
    if (Num == 1){
        printf("Enter new Name:\n");
        scanf("%s",&(temp->name));
    }
    else if (Num == 2){
        printf("Enter new Address:\n");
        scanf("%s",&(temp->address));
    }
    else if (Num == 3){
        printf("Enter new PoBox/P-Number:\n");
        scanf("%s",&(temp->PoBox));   
    }
    else if (Num == 4){
        printf("Enter new Name:\n");
        scanf("%s",&(temp->name));
        printf("\nEnter new Address:\n");
        scanf("%s",&(temp->address));
        printf("\nEnter new PoBox/P-Number:\n");
        scanf("%s",&(temp->PoBox)); 
        
    }
    Count=1;
}

void insert_user(int num)
{
    struct User *u = (struct User*)malloc(sizeof(struct User));
    u->number = num;
    if(j==0){
        printf("\n\n\n----********************-----\n");
        printf("**=> Hint:\nName:\t\tDavid,Jonson\n");
        printf("Address:\tStuvaregatan-22,Halmstad,Sweden,Lgh-105\n");
        printf("PoBox/P-Number:\t199912052255\n\n");
        
        printf("--------------------------------\nNo white space is acceptable\n--------------------------------\n");
        printf("----********************-----\n\n\n");
        j++;
    }
    
    printf("Enter First & last name:  ");
    scanf("%s", (u->name));

    printf("\nEnter address:  ");
    scanf("%s", (u->address));

    printf("\nEnter PoBox/P-number:  ");
    scanf("%s", (u->PoBox));

//    u->next = head;
//    head = u;
    if (head == NULL){
        head = u;
        u->next = NULL;
        }
    else {
        struct User *temp =head;
        while(temp->next != NULL){
            temp = temp->next;
            }
            temp->next = u;
            u->next = NULL;
        
    }
}
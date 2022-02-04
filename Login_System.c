#include <stdio.h>
#include <stdlib.h>
#include<windows.h>
#include<conio.h>
#include<string.h>
/* char f=getch();*/
int main()
{


    COORD a;
    a.X=40;
    a.Y=3;
    system("COLOR 20");
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Welcome to our site\n");

    getch();
    a.X=40;
    a.Y=10;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter 1 for SignUp\n");
    a.X=40;
    a.Y=11;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter 2 for Login\n");
    a.X=40;
    a.Y=12;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter 3 for Exit\n");
    a.X=40;
    a.Y=13;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter you choice");

    a.X=40;
    a.Y=14;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    int a1;
    scanf("%d",&a1);
    system("cls");
    switch(a1)
    {
     char s[100];
    case 1:

   a.X=40;
    a.Y=14;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter your email id");

    a.X=40;
    a.Y=15;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    scanf("%s",s);
    char g;



    a.X=40;
    a.Y=17;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Enter the password\n");
    a.X=40;
    a.Y=18;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    char q[100];
    int i=0;
    while(1)
    {
        char w=getch();

        if(w==13)
        {

            q[i]='\0';break;
        }
        else if(w==8)

        {
            i--;
            printf("\b \b");
        }
    else{
        q[i]=w;
        printf("*");i++;
    }

    }
    system("cls");
    a.X=40;
    a.Y=14;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Print Y if you want to see your ID and Password else print N for exit.");
    a.X=40;
    a.Y=15;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    char e;
     getchar();
    scanf("%c",&e);




    a.X=40;
    a.Y=16;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);

    if(e=='Y'){
    printf("Your email ID is  %s ",s);
    a.X=40;
    a.Y=17;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    printf("Your password is  %s",q);
      FILE *ptr=fopen("password.txt","w");
    int w=0;
    int yy=strlen(s);
    s[yy]='!';
    s[yy+1]='\0';
    int uu=strlen(q);
    q[uu]='%';
  q[uu+1]='\0';
    while(s[w]!='!')
    {

        putc(s[w],ptr);w++;
    }
    putc('!',ptr);
    w=0;
    while(q[w]!='%')
    {

        putc(q[w],ptr);w++;
    }
    putc('%',ptr);
    fclose(ptr);
    }
     else{
        FILE *ptr=fopen("password.txt","w");
    int w=0;
    int yy=strlen(s);
    s[yy]='!';
    s[yy+1]='\0';
    int uu=strlen(q);
    q[uu]='%';
  q[uu+1]='\0';
    while(s[w]!='!')
    {

        putc(s[w],ptr);w++;
    }
    putc('!',ptr);
    w=0;
    while(q[w]!='%')
    {

        putc(q[w],ptr);w++;
    }
    putc('%',ptr);
    fclose(ptr);
        exit(0);}


    break;
    case 2:
        system("cls");
         a.X=40;
         a.Y=14;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
       printf("Enter you email id");
        a.X=40;
        a.Y=15;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
       char dd[100];
       scanf("%s",dd);
       a.X=40;
       a.Y=16;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
       printf("Enter your password");
       a.X=40;
       a.Y=17;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);

    i=0;
    while(1)
    {
        char w=getch();

        if(w==13)
        {

            q[i]='\0';break;
        }
        else if(w==8)

        {
            i--;
            printf("\b \b");
        }
    else{
        q[i]=w;
        printf("*");i++;
    }

    }

    FILE *ptr=fopen("password.txt","r");
     a.X=40;
       a.Y=18;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
    if(ptr==NULL)
    printf("Something Went Wrong");
    else
    { char ch;i=0;
       int zz=strlen(dd);
       char t[100];
        while((ch=getc(ptr))!='!')
        {

              t[i]=ch;i++;


        }
        t[i]='\0';
        a.X=40;
       a.Y=18;

       SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
        if(strcmp(t,dd)!=0)
            printf("Wrong ID");
        else
        {
            int sss=strlen(q);i=0;char f[100];
            while((ch=getc(ptr))!='%')
            {


                f[i]=ch;i++;
            }
            f[i]='\0';
            if(strcmp(f,q)!=0)
            printf("Wrong Password");
            else
                printf("Login Successful");

        }

  fclose(ptr);
    }

  break;
    case 3:
        a.X=40;
    a.Y=18;

  SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),a);
        printf("Thank you so much. Have a nice day");
        exit(0);

    }
    getch();







}

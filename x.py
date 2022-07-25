from datetime import date
#ACCOUNT AND PIN INFO
def account():
    print("-------- ATM SYSTEM-------- ");
    atmno=str(input("Enter your Atm number= "));#ACCOUNT
    f=open("AccountInfo.txt","rt");
    global r;
    global i;
    r=f.readline();
    while r!="":
        for i in range(0,4):
            if r[i]!= atmno[i]:
                break;
            else:
                pass;
        if i==3:
            break;
        else:
            r=f.readline();
    else:
        print("Wrong Account Number!\nTry Again!");
        return;
    for n1 in range(3):#PIN
        if r!="":
            pin=str(input("Enter your pin number= "));
            for i in range(5,9):        
                if r[i]!= pin[i-5]:
                    break;
                else:
                    pass;
            #PIN CORRECT    
            if i==8:
                print("Welcome",end=" ");
                c=i+2;
                while r[c]!=".":
                    print(r[c],end="");
                    c=c+1;
                print("!");
                acc=r[0]+r[1]+r[2]+r[3];
                main_menu(acc);
                break;
            else:
                print("Wrong PIN Number!\nTry Again!");
    if n1==2:
        print("Wrong PIN Number!\nYour Pin nmber is incorrect 3 times!");
        return;
    else:
        return;

#FIRST PAGE
def main_menu(a):
    i=1;
    while(i!=0):
        print("-------- Main Menu --------");
        print(" 1. Balance Info");
        print(" 2. Withdraw Cash");
        print(" 3. Deposit Cash");
        print(" 4. Mini Statement");
        print(" 5. Exit");
        i=int(input(" Enter Your Choice= "));
        if i==1:
            balance_info(a);
        elif i==2:
            withdraw(a);
        elif i==3:
            deposit(a);
        elif i==4:
            mini(a);
        elif i==5:
            return;
        else:
            pass;
            
#BALANCE INFORMATION
def balance_info(a):
    acc=a+".txt";
    g=open(a,"rt")
    print("\nCurrent Balance= ");
    print(g.readline());
    g.close();
    t=0;
    while t!=5:
        print("Return to menu(press 5)= ");
        t=int(input());
        if t==5:
            return();

#WITHDRAW CASH
def withdraw(a):
    today=date.today();
    acc=a+".txt";
    g=open(a,"rt");
    bal=int(g.readline());
    temp=g.readline();
    t1=g.readline();
    t2=g.readline();
    t3=g.readline();
    t4=g.readline();
    g.close();
    g=open(a,"w");
    w=int(input("\n\nEnter the amount to be withdrawn= "));
    if w<int(bal):
        bal=bal-w;
        g.write(str(bal)+"\n");
        g.write(t1);
        g.write(t2);
        g.write(t3);
        g.write(t4);
        tempo="\n"+str(today)+" "+str(w)+" Withdrawn";
        g.write(tempo);
        print("\nTransaction is successful!");
    else:
        g.write(str(bal)+"\n");
        g.write(temp);
        g.write(t1);
        g.write(t2);
        g.write(t3);
        g.write(t4);
        print("\nTransaction is unsuccessful!");
    g.close();

#DEPOSIT CASH
def deposit(a):
    today=date.today();
    acc=a+".txt";
    g=open(a,"rt");
    bal=int(g.readline());
    temp=g.readline();
    t1=g.readline();
    t2=g.readline();
    t3=g.readline();
    t4=g.readline();
    g.close();
    g=open(a,"w");
    w=int(input("\n\nEnter the amount to be deposited= "));

    bal=bal+w;
    g.write(str(bal)+"\n");
    g.write(t1);
    g.write(t2);
    g.write(t3);
    g.write(t4);
    tempo="\n"+str(today)+" "+str(w)+" Deposit";
    g.write(tempo);
    print("\nTransaction is successful!");

    g.close();

#MINI STATEMENT
def mini(a):
    today=date.today();
    acc=a+".txt";
    g=open(a,"rt");
    bal=int(g.readline());
    temp=g.readline();
    t1=g.readline();
    t2=g.readline();
    t3=g.readline();
    t4=g.readline();
    
    print("\n\nMini Statement:- ");
    print("Date=",today);
    print("Balance=",bal);
    print(temp,end="");
    print(t1,end="");
    print(t2,end="");
    print(t3,end="");
    print(t4,end="");
    print("\nTransaction is successful!");

    g.close();
    t=0;
    while t!=5:
        print("\n\nReturn to menu(press 5)= ");
        t=int(input());
        if t==5:
            return();
        
#MAIN PROGRAM        
exist=1;        
while exist==1:
    account();    

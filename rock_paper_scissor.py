import random
c1=0
c2=0
while True:
    choice=int(input("Enter your choice\n1.Rock\n2.Paper\n3.Scissor:\n"))
    while choice>3 | choice<1:
        choice=int(input("Enter valid choice"))
    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    elif choice==3:
        choice_name="Scissor"
    print("Your choice:%s"%choice_name)
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    elif comp_choice==3:
        comp_choice_name="Scissor"
    print("Computer's Choice:{b}".format(b=comp_choice_name))
    if(choice==1 and comp_choice==2):
        c1=c1+1
        print("Computer Wins!")
    elif(choice==2 and comp_choice==3):
        c1=c1+1
        print("Computer Wins!")
    elif(choice==3 and comp_choice==1):
        c1=c1+1
        print("Computer Wins!")
    elif((choice==1 and comp_choice==1) or (choice==2 and comp_choice==2) or (choice==3 and comp_choice==3)):
        print("It's a draw")
    else:
        print("You Win!")
        c2=c2+1
        
    print("Do you want to play again(y/n)")
    ans=input()
    if ans=="n" or ans=="N":
        print("Your Score:{a} Computer Score:{b} ".format(a=c2,b=c1))
        break

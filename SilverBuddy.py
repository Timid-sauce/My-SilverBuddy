'''
SilverBuddy Program
Technica 2017
'''
import os.path
Spending = []

endProgram = 0

print("Welcome to Your Personal SilverBuddy!")
print("To begin you have 3 options: \n")
option = input("Option 1: Take a Quiz to figure out your spending habits \nOption 2: Go to your personal SilverMonitor® \nOption 3: See your past spending days\
\nPress 1 , 2 , or 3 based on the option you select. ")

def SilverMoniter():
    Spending = readFile()
    for i in range(len(Spending)+1,32):
        print("Day", i)
        money = input("How much money did you spend today?(In US Dollars) Ex:$0.48 ")
        print(money)
        if money == 'q':
            print("You have chosen to quit the program")
            break
        Spending.append(money)
    writeFile()
def readFile():
    if os.path.isfile('SpendingPast.txt'):
        my_file = open('SpendingPast.txt','r')
        line = my_file.readline()
        if line == '':
            return []
        return line.split(",")
    else:
        return []
def writeFile():
    f = open('SpendingPast.txt','w+')
    line = f.write(','.join(Spending))
    f.close()
import time
def countdown(n):
    print(" \nLoading...")
    while n > 0:
        time.sleep(1)
        n = n - 1
        
if option == '1':
    quiz = str(input("\nAre you sure you want to take the quiz? \n(Enter Yes or No - Capitalization doesn't matter)"))
    if quiz.upper() == 'NO':
        print(" Ok!")
        countdown(3)
        print("Menu has loaded SUCCESSFULLY. \n")
        print("To begin you have 3 options: \n")
        option = input("Option 1: Take a Quiz to figure out your spending habits \
    \nOption 2: Go to your personal MoneyMonitor® \nOption 3: See your past spending days\
    \nPress 1 , 2 , or 3 based on the option you select. ")
        if option == '1':
            print("Ok your quiz will begin shortly.")
            countdown(3)
            print("Your quiz has loaded SUCCESSFULLY.")
            school = input("\n What level of schooling are you in? \
        \n\t a. High School \
        \n\t b. Under Grad \
        \n\t c. Post Grad")
            form = input("\n What form of money qdo you use most often? \
        \n\t a. Debit \
        \n\t b. Credit \
        \n\t c. Cash")
            job = input("\n Do you have a job? (Paid internships included)\
        \n\t a. Yes \
        \n\t b. No ")
            if job.upper() == 'A':
                paid = input("\n How much are you paid monthly? \
        \n\t a. < 3,000 \
        \n\t b. 3,000 - 15,000\
        \n\t c. 15,000 - 24,000 \
        \n\t d. 24,000 - 36,000 \
        \n\t e. > 36,000")
                print("All ready to go! Let's begin Tracking!")
                previousUse = input("Have you used MySilverBuddy® before? (Please enter Yes or No - Capitalizaton doesn't matter)")
                if previousUse.upper() == 'YES':
                    print("Great! Let's jump right into it!")
                    SilverMoniter()
                elif previousUse.upper() == 'NO':
                    countdown(3)
                    print("Your tutorial has loaded SUCCESSFULLY")
                    input("Your SliverMonitor® will ask you how much money you have spent. (Press ENTER to continue)")
                    input("Then it will show you how many days you have spent money so you ca manage your money.(Press enter to continue)")
                    tutorial = input(" Do you understand how to use SilverMonitor® ? (Answer YES or NO - Capitalization does NOT matter)")
                    if tutorial.upper() == 'YES':
                        print("Okay! Let's Begin!")
                        SilverMonitor()                       
            if job.upper() == 'B':
                print("All ready to go! Let's begin Tracking!")
                previousUse = input("Have you used MySilverBuddy® before? (Please enter Yes or No - Capitalizaton doesn't matter)")
                if previousUse.upper() == 'YES':
                    print("Great! Let's jump right into it!")
                    SilverMoniter()
                elif previousUse.upper() == 'NO':
                    countdown(3)
                    print("Your tutorial has loaded SUCCESSFULLY")
                    input("Your SilverMonitor® will ask you how much money you have spent. (Press ENTER to continue)")
                    input("Then it will show you how many days you have spent money so you ca manage your money.(Press enter to continue)")
                    tutorial = input(" Do you understand how to use SilverMonitor® ? (Answer YES or NO - Capitalization does NOT matter)")
                    if tutorial.upper() == 'YES':
                        print("Okay! Let's Begin!")
                        SilverMonitor()
        if option == '2':
            print ("Silver Moniter")
            SilverMoniter()
            print (str(Spending))

        if option == '3':
            print (str(Spending))
            
    elif quiz.upper() == 'YES':
        print("Ok your quiz will begin shortly.")
        countdown(3)
        print("Your quiz has loaded SUCCESSFULLY.")
        school = input("\n What level of schooling are you in? \
    \n\t a. High School \
    \n\t b. Under Grad \
    \n\t c. Post Grad")
        form = input("\n What form of money do you use most often? \
    \n\t a. Debit \
    \n\t b. Credit \
    \n\t c. Cash")
        job = input("\n Do you have a job? (Paid internships included)\
    \n\t a. Yes \
    \n\t b. No ")
        if job.upper() == 'A':
            paid = input("\n How much are you paid monthly? \
    \n\t a. < 3,000 \
    \n\t b. 3,000 - 15,000\
    \n\t c. 15,000 - 24,000 \
    \n\t d. 24,000 - 36,000 \
    \n\t e. > 36,000 \ ")
            print("All ready to go! Let's begin Tracking!")
            previousUse = input("Have you used MySilverBuddy® before? (Please enter Yes or No - Capitalizaton doesn't matter)")
            if previousUse.upper() == 'YES':
                print("Great! Let's jump right into it!")
                SilverMoniter()
            elif previousUse.upper() == 'NO':
                countdown(3)
                print("Your tutorial has loaded SUCCESSFULLY")
                input("Your SliverMonitor® will ask you how much money you have spent. (Press ENTER to continue)")
                input("Then it will show you how many days you have spent money so you ca manage your money.(Press enter to continue)")
                tutorial = input(" Do you understand how to use SilverMonitor® ? (Answer YES or NO - Capitalization does NOT matter)")
                if tutorial.upper() == 'YES':
                    print("Okay! Let's Begin!")
                    SilverMoniter()
                else:
                    print("Oh No! Maybe this isn't the right program for you!")
                    endProgram = 1
        if job.upper() == 'B':
            print("All ready to go! Let's begin Tracking!")
            previousUse = input("Have you used MySilverBuddy® before? (Please enter Yes or No - Capitalizaton doesn't matter)")
            if previousUse.upper() == 'YES':
                print("Great! Let's jump right into it!")
                SilverMoniter()
            elif previousUse.upper() == 'NO':
                countdown(3)
                print("Your tutorial has loaded SUCCESSFULLY")
                input("Your SliverMonitor® will ask you how much money you have spent. (Press ENTER to continue)")
                input("Then it will show you how many days you have spent money so you ca manage your money.(Press enter to continue)")
                tutorial = input(" Do you understand how to use SilverMonitor® ? (Answer YES or NO - Capitalization does NOT matter)")
                if tutorial.upper() == 'YES':
                    print("Okay! Let's Begin!")
                    SilverMoniter()
                else:
                    print("Oh No! Maybe this isn't the right program for you!")
                    endProgram = 1
    
elif option == '2':
    print ("Silver Moniter")
    SilverMoniter()

elif option == '3':
    print (str(Spending))
    
else:
    print("You have entered an invalid response.")

import sys

def bold(type): 
    sys.stdout.write("\033[1m" + type + "\033[0m")

bold("Welcome to the best Math Calculator")
print("\n" * 20)

mathinput = float(input("enter in your number to calculate: "))
mathtype = input("What math concept do you want to do with your number (math concepts that we support is multiplication, division, addition and subtraction) ")
if mathtype == "multiplication":
    mathinput2 = float(input("What number should your previous number be multiplied by? "))
    mathinput *= mathinput2
    print("\n" * 100)
    print("Your answer is " + str(mathinput))
    print("Thank You for using Math Calculator by Aditya D")
    choicei = input("Do you want to multiply again (Y) or choose another math concept to use (N): ")
    while choicei == "Y":
        rmathinput = float(input("enter in your number to calculate: "))
        rmathinput2 = float(input("What number should your previous number be multiplied by? "))
        rmathinput *= rmathinput2
        print("\n" * 100)
        print("Your answer is " + str(rmathinput))
        print("Thank You for using Math Calculator by Aditya D")
        choicei = input("Do you want to multiply again (Y) or choose another math concept to use (N): ")

if mathtype == "addition":
    mathinput2 = float(input("What number should your previous number be added by? "))
    mathinput += mathinput2
    print("\n" * 100)
    print("Thank you for using Math Calculator by Aditya D")
    print("Your answer is " + str(mathinput))
    choicei = input("Do you want to add again (Y) or choose another math concept to use? (N) ")
    while choicei == "Y":
        rmathinput = float(input("enter in the number to calculate: "))
        rmathinput2 = float(input("What number should your previous number be added by: "))
        rmathinput += rmathinput2
        print("Thank you for using Math Calculator by Aditya D")
        print("your answer is " +  str(rmathinput))
        choicei = input("Do you want to add again (Y) or choose another math concept to use? (N) ")

if mathtype == "subtraction":
    mathinput2 = float(input("What number should your previous number be subtracted by: "))
    mathinput -= mathinput2
    print("\n" * 100)
    print("Thank You for using Math Calculator by Aditya Dani")
    print("Your answer is " + str(mathinput))
    choicei = input("Do you want to subtract again (Y) or choose another math concept to use? (N) ")
    while choicei == "Y":
        rmathinput = float(input("enter in the number to calculate: "))
        rmathinput2 = float(input("What number should your previous number be subtracted by: "))
        rmathinput -= rmathinput2
        print("\n" * 100)
        print("Thank you for using Math Calculator by Aditya D")
        print("Your answer is " + str(rmathinput))
        choicei = input("Do you want to subtract again (Y) or choose another math concept to use? (N) ")

if mathtype == "division":
    mathinput2 = float(input("What number should your previous number be divided by: "))
    mathinput /= mathinput2
    print("\n" * 100)
    print("Thank you for using Math Calculator by Aditya D")
    print("Your answer is " + str(mathinput))
    choicei = input("Do you want to divide again (Y) or choose another math concept to use? (N) ")
    while choicei == "Y":
        rmathinput = float(input("enter in the number to calculate: "))
        rmathinput2 = float(input("What number should your previous number be divided by: "))
        rmathinput /= rmathinput2
        print("\n" * 100)
        print("Thank you for using Math Calculator by Aditya D")
        print("Your answer is " + str(rmathinput))
        choicei = input("Do you want to divide again (Y) or choose another math concept to use? (N)")

while choicei == "N":
    mathinput = float(input("enter in your number to calculate: "))
    mathtype = input("What math concept do you want to do with your number (math concepts that we support is multiplication, division, addition and subtraction) ")
    if mathtype == "multiplication":
        mathinput2 = float(input("What number should your previous number be multiplied by? "))
        mathinput *= mathinput2
        print("\n" * 100)
        print("Your answer is " + str(mathinput))
        print("Thank You for using Math Calculator by Aditya D")
        choicei = input("Do you want to multiply again (Y) or choose another math concept to use (N): ")
        while choicei == "Y":
            rmathinput = float(input("enter in your number to calculate: "))
            rmathinput2 = float(input("What number should your previous number be multiplied by? "))
            rmathinput *= rmathinput2
            print("\n" * 100)
            print("Your answer is " + str(rmathinput))
            print("Thank You for using Math Calculator by Aditya D")
            choicei = input("Do you want to multiply again (Y) or choose another math concept to use (N): ")

    if mathtype == "addition":
        mathinput2 = float(input("What number should your previous number be added by? "))
        mathinput += mathinput2
        print("\n" * 100)
        print("Thank you for using Math Calculator by Aditya D")
        print("Your answer is " + str(mathinput))
        choicei = input("Do you want to add again (Y) or choose another math concept to use? (N) ")
        while choicei == "Y":
            rmathinput = float(input("enter in the number to calculate: "))
            rmathinput2 = float(input("What number should your previous number be added by: "))
            rmathinput += rmathinput2
            print("Thank you for using Math Calculator by Aditya D")
            print("your answer is " +  str(rmathinput))
            choicei = input("Do you want to add again (Y) or choose another math concept to use? (N) ")

    if mathtype == "subtraction":
        mathinput2 = float(input("What number should your previous number be subtracted by: "))
        mathinput -= mathinput2
        print("\n" * 100)
        print("Thank You for using Math Calculator by Aditya Dani")
        print("Your answer is " + str(mathinput))
        choicei = input("Do you want to subtract again (Y) or choose another math concept to use? (N) ")
        while choicei == "Y":
            rmathinput = float(input("enter in the number to calculate: "))
            rmathinput2 = float(input("What number should your previous number be subtracted by: "))
            rmathinput -= rmathinput2
            print("\n" * 100)
            print("Thank you for using Math Calculator by Aditya D")
            print("Your answer is " + str(rmathinput))
            choicei = input("Do you want to subtract again (Y) or choose another math concept to use? (N) ")

    if mathtype == "division":
        mathinput2 = float(input("What number should your previous number be divided by: "))
        mathinput /= mathinput2
        print("\n" * 100)
        print("Thank you for using Math Calculator by Aditya D")
        print("Your answer is " + str(mathinput))
        choicei = input("Do you want to divide again (Y) or choose another math concept to use? (N) ")
        while choicei == "Y":
            rmathinput = float(input("enter in the number to calculate: "))
            rmathinput2 = float(input("What number should your previous number be divided by: "))
            rmathinput /= rmathinput2
            print("\n" * 100)
            print("Thank you for using Math Calculator by Aditya D")
            print("Your answer is " + str(rmathinput))
            choicei = input("Do you want to divide again (Y) or choose another math concept to use? (N) ")







        

import time

while True:
    time.sleep(2)
    print("\n                -----PRIME NUMBER TOOL--------             ")
    print("\nYou have 3 choices here")
    print("\n1. You can check whether a number is prime or not.")
    print("2. You can check a prime number till some number.")
    print("3. \"exit\" which will exit the the programm.")
    try:

        user_choice = int(input("\nEnter the choice 1/2/3 : ")).strip()

    except ValueError:
        print("Please type btw 1,2 and 3")
        continue


    if(user_choice == 1):

        try:

            n = input("\nEnter the number you want to know is prime or not: ")
            
            N = int(n)
            if(N<=1):
                print(f"{N} is not a prime number")
                continue

            for i in range(2,N):
                if(N%i==0):
                    print(f"{N} is not a prime number.")
                    break
            else:
                print(f"{N} is a prime number.")  

             
        except ValueError:
            print("\nERROR Please type an valid number.")

            
    elif(user_choice == 2):


        try:


            n = input("enter the number you want prime number untill: ")
            N = int(n)
            for i in range(2,N+1):
                for j in range(2,i):
                    if(i%j==0):

                        break
                else:
                    print(f"{i} is a prime number")
        except ValueError:
            print("ERROR please type valid number")

    
    
    
    elif(user_choice==3):

        print("\nExiting the programm..." \
        "\nHave a nice day")
        break

    else:
        print("Please enter valid choice.")






    

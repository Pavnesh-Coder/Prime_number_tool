while True:
    n = input("\nEnter the number you want to know is prime or not:\n(or type \"exit\" to leave the programm) ")
    if(n== "exit"):
        print("Exiting the programm..")
        print("Thank you have a nice day.")
        break
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
        




n=int(input("Enter no:"))
if n<0:
    print("Add positive no:")
elif n==0:
    print("can't able to find factorial of 0")
else:
    factorial=1
    for i in range(1,n+1):
        factorial *=i
    print(factorial)

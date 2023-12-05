count=0
summ=0
while True:
    num=int(input("Enter number:"))
    if num==0:
        break;
    count +=1
    summ=summ+num
avg=summ /count
print(summ,avg)    

    
n=int(input("Enter no:"))
even=0
esum=0
odd=0
osum=0
while n > 0:
        digit = n % 10
      
        if digit % 2 == 0:
            even += 1
            esum += digit
        else:
            odd += 1
            osum += digit
        n //= 10
print(even)
print(esum)
print(odd)
print(osum)
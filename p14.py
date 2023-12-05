cp=int(input("Enter the cost price of product:"));
sp=int(input("Enter the sell price of product:"));
a=cp-sp
if a>0:
	print("Profit:", a)
else:
	print("Loss:", +(a))
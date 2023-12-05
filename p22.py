s1=int(input("Enter marks subject1:"))
s2=int(input("Enter marks subject2:"))
s3=int(input("Enter marks subject3:"))
s4=int(input("Enter marks subject4:"))
s5=int(input("Enter marks subject5:"))
total=s1+s2+s3+s4+s5
per=(total*500)/100
if per>=75:
    print("Distinction")
elif per>=60 and per<70:
    print("firstclass")
elif per>=50 and per<60:
    print("second class")
elif per>=40 and per<50:
    print("pass class")
else:
    print("fail")
c=int(input("Enter employee's unique code:"))
s=int(input("Enter basic salary:"))
if c>0 and c<=5:
    da=(s*60)/100
    ma=(s*12)/100
    pf=(s*10)/100
    it=(s*15)/100
    nets=s+da+ma-pf-it
    print("net salary:",nets)
elif c>5 and c<=12:
    da=(s*65)/100
    ma=(s*10)/100
    pf=(s*9)/100
    it=(s*10)/10014
    nets=s+da+ma-pf-it
    print("net salary:",nets)
elif c>12 and c<=15:
    da=s*(55/100)
    ma=s*(8/100)
    pf=s*(8/100)
    it=s*(8/100)
    nets=s+da+ma-pf-it
    print("net salary:",nets)
else:
    print("Enter valid employee's unique code")
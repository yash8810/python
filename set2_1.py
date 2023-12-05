p1=int(input("Enter marks of paper1:"))
p2=int(input("Enter marks of paper2:"))
p3=int(input("Enter marks of paper3:"))
c=input("Enter category:")
if p1<100 and p2<100 and p3<100:
    if p1<=50 and p2<=50 and p3<=50:
        total=p1+p2+p3
        per=(total*3)/10054
        if c=='st'  and per<=45: 
                print("qualified")
        else:
              print("unqualified")
        if c=='sc' and c=='SC':
                print("qualified")
        else:
              print("qualified")
        if c=='obc' and c=='OBC':
                 print("qualified")
        else:
              print("qualified")
        if c=='open' and c=='OPEN':
            print("qualified")
        else:
              print("qualified")
    else:
          print("unqualified")
else:
    print("enter proper marks.")
    
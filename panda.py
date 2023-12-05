import pandas as pd
def grade(df):
    if(df['percentage']<40):
         return("f")
    elif(df['percentage']>=40 and df['percentage']<50):
        return ("c")
    elif(df['percentage']>=50 and df['percentage']<60):
        return ("b")
    else:
        return ("a")
def result(df):
    if(df['percentage']<40):
         return("fail")
    elif(df['percentage']>=40 and df['percentage']<50):
        return ("pass")
    elif(df['percentage']>=50 and df['percentage']<60):
        return ("second")
    else:
        return ("first")
df=pd.read_csv('mark.csv')

# print(df)
df['total']=df['m1']+df['m2']
df['percentage']=(df['total']*100)/200
df['grade']=df.apply(grade,axis=1)
df['result']=df.apply(result,axis=1)
m=df[df['percentage']==df['percentage'].max()]['name'].values[0]
m1=df[df['percentage']==df['percentage'].min()]['name'].values[0]
print("1st rank:",m)
df.to_csv('mmarks.csv')
df.to_csv('result3.csv')
print(df)
print("1st rank:",m)
print("last rank:",m1)






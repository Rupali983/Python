def sum(x,y):
    return x+y
def Subtract(x,y):
    return x-y 
def multi(x,y):
    return x*y 
def division(x,y):
    return x/y 
print("select option \n" \
      "1.sum\n" \
       "2.subtract\n" \
       "3.multi\n"\
        "4.division/n")
select=int(input("select optration from1,2,3,4:"))
x=int(input("enter a number="))
y=int(input("enter a number="))
if  select==1:
    print(x,"+",y,"=",sum(x,y))
elif select==2:
    print(x,"-",y,"=",Subtract(x,y))
elif select==3:
    print(x,"*",y,"=",multi(x,y))
elif select==4:
    print(x,"/",y,"=",division(x,y))
else:
    print("invaild input")

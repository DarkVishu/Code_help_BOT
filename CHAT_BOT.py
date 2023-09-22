#common logical programs with examples...
b="chatGUDDU : "
print("Hello Begineer!! ","chatGUDDU here ^_^","","I was designed by sir Vishu.","You can take my help anytime,","Whenever you get stuck with your python codes.","And i am  still being updated...!","","chatGUDDU : ohh! it seems you are first time here!",sep="\n" )
a=input("what's your good name : ")
print(b,"Hii %s"%a)
print(a,end=" ")
input(": ")
print("chatGUDDU : Nice talking to you %s.. "%a,"Are you facing trouble in programing..?","Do you need some help ? Y/N",sep="\n            ")
print(a,end=" ")
q=input(": ")
if q=="y" or q=="yes" or q=="Y" or q=="YES" or q=="Yes":
    print("chatGUDDU : Here's what i have for you...","You can select among these...","What you want..","1. Check ODD or EVEN ?","2. Check PRIME ?","3. Check LEAP ?","4. Find FACTORIAL ?","5. Print FIBONACI series ?","6. Check ARMSTRONG ?",sep="\n            ")
    c=int(input("Enter a choice  : "))
    if c>=1 and c<=10:
        print("%sHere comes your code..."%b)
        if (c==1):
            {print("\n","a=int(input('Enter a number : '))\n","print('EVEN' if a%2==0 else 'ODD')\n",sep=" "*12)}
        elif (c==2):
            {print("\n","a=int(input('Enter a number : '))\n","count=0\n","for i in range (1,a+1):\n", "    if n%i==0:\n","         count+=1\n","print('PRIME' if count==2 else 'not PRIME')",sep=" "*12)}
        elif (c==3):
            {print("\n","def is_leap(year):\n","    if year%100==0:\n","        if year%400==0:\n","            leap=True\n","        else:\n","            leap=False\n","    elif year%4==0:\n","        leap=True\n","    else:\n","        leap=False\n","    return leap\n","\n","year = int(input('Enter a year'))\n","print(is_leap(year))",sep=" "*12)}
        elif (c==4):
            {print("\n","a=int(input('Enter a number : '))\n","c=1\n","for i in range (1,a+1):\n","     c=c*i\n","print(c)",sep=" "*12)}
        elif (c==5):
            {print("\n","a=int(input('Enter a number : '))\n","b=0\n","c=1\n","for i in range (a):\n","    print('%d'%b,end=' ')\n","    x=b+c\n","    b=c\n","    c=x",sep=" "*12)}
        elif (c==6):
            {print("\n","a=int(input('enter a number :'))\n","b=str(a)\n","c=len(b)\n","x=0\n","for i in b:\n","    i=int(i)\n","    d=i**c\n","    x=x+d\n","print('ARMSTRONG' if x==a else 'not ARMSTRONG' )",sep=" "*12)}
        else:
            print("%sSorry %s invalid input...!!"%(b,a))
    elif q=="n" or q=="no" or q=="N" or q=="NO" or q=="No":
        print("chatGUDDU : Thank you for using me...\n"," it's my pleasure to serve you.",sep=" "*12)
    else:
        print("%sSorry %s invalid input...!!"%(b,a))
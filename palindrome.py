n=int(input("enter the number"))
res=0
a=n
while(n!=0):
    temp=n%10
    res=res*10+temp
    n=n//10
if(a==res):
    print("palindrome")
else:
    print("not a palindrame")
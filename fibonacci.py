num=int(input("Enter a number"))
n1=0
n2=1
count=0
if num<=0:
    print("Enter a number greater than zero")
elif num==1:
    print("Fibonacci series: ",n1)
else:
    print("Fibonacci series: ")
    while count<num:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
        

#question1 
for i in range(2,11,2):
    print(i)

#question2
sum=0
for i in range(1,11,2):
    sum+=i
    print(sum)

#question3
a=0
b=1
while a<=50:
    print(a,end=" ")
    c=a+b
    a=b
    b=c    

#question4
A=input("enter a string=")
result=""
for x in range(len(A)):
    if x%2==0:
        result+=A[x]
        print(result)
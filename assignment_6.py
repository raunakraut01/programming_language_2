'''question1'''
a=[10,20,30,40,50,60,70,80,90,100]
x=int(input("enter a number to check="))
if x in a:
    print("number is present in list")
else:
    print("number is not present in list ")

if x not in a :
    print("number is not present in list")
else:
    print("number is present in list ")

'''question2'''
A=["python","is","a","programming","language"]
#indexing
print(A[3])
#negative indexing
print(A[-2])
#slicing
print(A[2:4])

'''question3'''
sport=["cricket","football","hockey","tennis"]
#update
sport[2]="badminton"
print(sport)
#append
sport.append("volleyball")
print(sport)
#insert
sport.insert(1,"baseball")
print(sport)
#delete
del sport[3]
print(sport)

'''question4'''
list1=["cricket","football","volleyball"]
list2=["tennis","badminton","baseball"]
#concatenation
list3=list1+list2
print(list3)
#repetition
list4=list1*3
print(list4)
#length
print(len(list2))
#maximum
print(max(list3))
#minimum
print(min(list1))
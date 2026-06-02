#question1 
from math import dist


d={'a':3, 'b':1,'c':2}
asc=dict(sorted(d.items(),key= lambda x:x[1]))
desc=dict(sorted(d.items(),key= lambda x:x[1],reverse=True))
print("ascending order=",asc)
print("descending order=",desc)

#question 2
d={'name','Raunak','age', '19'}
key=input("Enter a key:")
if key in d:
    print("key exists")
else:
    print("key does not exists")

#question 3
d1={'a':1, 'b':2,'c':3}
d2={'d':4, 'e':5}
d1.update(d2)
print(d1)

#question 4
t=(1,2,3)
t1=t + (4,)
print("updated tuple:",t1)

#question 5
t=(10,"hello",3.14,True)
print("tuple:",t)

#question6
list=[10,20,30,40]
total=sum(list)
print("sum:", total ) 

#question7
list=[5,10,15,20]
large=max(list)
print("largest number:",large)

#question8
s={1,2,3}
s.add(4)
s.update([5,6])
print("updated set:",s)

#question9
arr=[1,2,3,4,5]
arr.reverse()
print(arr)

#question10
arr=[1,2,3,4,5]
print(arr[0])
print(arr[3])
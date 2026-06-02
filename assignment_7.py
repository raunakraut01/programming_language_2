#question 1
a=[2,4,6,8,10]
b=[1,3,5,7,9]
print(len(a))
print(len(b))
c=a+b
print(c)
print(a*2)
print(4 in a)
print(3 not in a)
print(40 in(c))

#question 2
a=(2,3,4,5,6,7,8,9)
print(a[3])
print(a[-3])
print(a[:6])
print(a[1: ])
for i in a:
    i+=1
    print(i)

#question 3
a=(5,10,15,20)
b=(7,14,21,28)
print(a+(29,))

del b 
print("deleted successfully")

#question4
a=(2,4,6,8)
b=(1,3,5,7)
f=["mango","apple","Banana"]
print(len(a))
print(max(b))
print(min(a))
print(tuple(f))
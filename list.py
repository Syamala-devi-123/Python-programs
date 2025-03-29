#empty list
a=[ ]
print(a)

#Duplication
a=[1,2,3,4,4]
print(a)

#indexing
a=["lav",7,3,8,True]
print(a[0])
print(a[-1])
print(int(True))
print(bool(1))
print(bool(0.0))
print(bool(2))
print(bool(-1))


#List methods
#len function
a=[10,20,30,40,50]
print(len(a))
lav=[]
print(len(lav))

#append
a=[10,20,30,40,50]
l=a.append(60)
print(a)

l=a.append(30)
print(a)

l=a.append("sai")
print(a)
#insert
a=["lav","sai"]
l=a.insert(1,"puji")
print(a)
l=a.insert(2,"om")
print(a)

#Indexing
a=["lav",1,"good"]
print(a.index("lav"))

#Extending
a=[1,2,9]
b=[3,4,8,9]
l=a.extend(b)
print(a)
a=[1,2,3]
b=[7,8,6]
l=a.extend(b)
print(a)

#Traversing of a list
a=[1,True,"sai",2.2]
for i in a:
    print(i,end='')
a=[1,True,"sai",2.2]
for i in a:
    print(i)
a=[1,True,"sai",2.2]
for i in a:
    print(i in a)


#sum of numbers in a list i's sum
a=[1,2,3,4]
sum=0
for i in a:
    sum+=i
    print(sum)
#total sum of a list    
a=[1,2,3,4]
sum=0
for i in range(1,5):
    sum+=i
print(sum)    
#another method
a=[1,2,3,4]
b=[5,6,7,8]
print(sum(a+b))
   


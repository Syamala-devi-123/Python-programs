#patterns
#solid square
n=10
for i in range(n):
    print("* "*n)
    
#solid Rhambus pattern
n=10
for i in range(n):
    print(" "*i+"* "*n)
    
#Hallow square
n=10
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n)
    else:
        print("*"+"  "*(n-2)+" *")
        
# Right angle triangle
n=10
for i in range(n):
    print("* "*i)


#reverse right angle triangle
n=10
for i in range(n):
    print("* "*n)
    n-=1

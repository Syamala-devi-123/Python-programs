#cars
n=int(input("Enter No. of persons:")) 
if n%4==0:
    cars = n//4
    print("Cars required:",cars)
else:
    cars = (n//4)+1
    print("Cars required:",cars)



#road tax
n=int(input())
if 1<=n<=10:
    print(n*10)
elif 11<=n<=20:
    print(n*12)
elif 20<=n<=30:
    print(n*15)
elif n>31:
    print("hema will collect charge")

#swapping without third variable
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)



#area of triangle using heroins formula
import math
a=int(input())
b=int(input())
c=int(input())
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area=math.sqrt(s*(s-a)(s-b)(s-c))
    print(area)
else:
    print("invalid input")


#converting the distance

km=float(input())
print("The km is :",km)
meters =km*1000
print("The meters is :",meters)
centimeters=km*100000
print("The centimeters is :",centimeters)
feet=km*3280.84     
print(" the feet is:",feet)
inches=km*39370.1 
print(" the inches is :",inches)    

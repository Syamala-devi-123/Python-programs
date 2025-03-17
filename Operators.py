#operators
#arthmetic operator
a=10
b=5
print(a+b)#addition
print(a-b)#sub
print(a*b)#mul
print(a/b)#div
print(a%b)#mod div
print(a//b)#floor divivson
print(a**b)#exponential

"""
hi
hello
these is the multiline comment 
"""
#multiline string
a=""" hi
      hello
      good morning
   """
print(a)


#assignment operators
a=2
b=2
c=a+b
print(c)#=
a=2
b=3
b+=a #augmented assignment operator
print(b)
a=2
b=4
b-=a #b=b-a
print(b)
b*=a#b=b*a
print(b)
b/=a#b=b/a
print(b)
a=2
b=4
b%=a
print(b)
a=2
b=4
b//=a
print(b)
b**=a#b=b*a
print(b)


#relational operators
a=10
b=30
print(a>b)#greater than
print(a<b)#less than
print(a>=b)#greater than or equal to
print(a<=b)#lesser than or equal
print(a==b)#equal
print(a!=b)#not equal to


#Logical operators and ,or,not
a=10
b=20
print(a and b)#high
print(a or b)#low
print(not b)#belongs to one variable
print(a>b and a<b)
print(a<b and b>a)
print(a>b or b>a)
print(a>b or b<a)
print(not a>b)
print(a>b and b<a or a<b)


#Identity operator,is ,isnot
a=10
b=20
print(a is b)
print(a is not b)
a=10
b=10
print(a is b)
print(a is not b)

#membership operator
a=[1,2,3,4]
print(4 in a)
print(10 not in a)
print(5 in a)
print(3 not in a)

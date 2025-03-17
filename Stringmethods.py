#string methods
a=input()
#indexing:access the particular element through index positioning(single element)
print(a[0])
print(a[5])
#slicing:access the particular elements through index it has three parameters start,end,step(multiple elements)
print(a[0:5])
print(a[0: 10 :2])
print(a[1: : 2])
#reverse:negative indexing using
print(a[-1])
print(a[-1: ])

#length
print(len(a))

#split function(list)
a=input()
print(a.split( ))
print(a.split('c'))
print(a.split('j'))
print(a.split('p'))

#strip function(remove spaces and letters)
a=input()
print(a.strip())
print(a.strip('a'))
print(a.strip('ya'))
print(a.strip('va'))

a=input()
#isdigit()
print(a.isdigit())
#isupper()
print(a.isupper())
#islower()
print(a.islower())
#alphanum()
print(a.isalnum())
a=input()
#.upper()
print(a.upper())
a=input()
#.lower()
print(a.lower())
#startswith()
print(a.startswith('LAV'))
#endswith()
print(a.endswith('nya'))
#.join
a=[1,2,3]
print(",".join(map(str, a)))


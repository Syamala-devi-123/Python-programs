s=input()
print(s.replace(" ",""))
rev=s[-1: :-1]
if rev==s:
    print("palindrome")
else:
    print("Not palindrome")

#hand game -rock paper secissor
a=input()
b=input()
if(a=='rock' and b=='paper'):
    print("a is winner")
elif(a=='rock' and b=='secissor'):
    print("a is winner")
elif(a=='paper' and b=='secissor'):
    print("b is winner")
elif(a=='paper' and b=='rock'):
    print("b is winner")
elif(a=='secissor' and b=='paper'):
    print("a is winner")
elif(a=='secissor' and b=='rock'):
    print("b is winner")
elif(a=='rock' and b=='rock'):
    print("tie")    
elif(a=='secissor' and b=='secissor'):
    print("tie")
elif(a=='paper' and b=='paper'):
    print("tie")        
    

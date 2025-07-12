n=int(input())
list1=[]
for i in range(n):
    command=input()
    list1.append(command)
i=0
stack=[]
top=0
reg=0
while i != n+1:
    text=list1[i]

    if "PUSH" in text:
        wordlist=text.split()
        
        num=int(wordlist[1])
        stack.append(num)
        i+=1
        
    elif text=="STORE":
        reg=stack[-1]
        
        stack.pop()
        i+=1
    elif text=="LOAD":
        stack.append(reg)
        i+=1
        
    elif text=="PLUS":
        num1=stack[-1]
        stack.pop()
        
        num2=stack[-1]
        stack.pop()
        stack.append(num1+num2)
        i+=1
    elif text=="TIMES":
        num1=stack[-1]
        stack.pop()
        
        num2=stack[-1]
        stack.append(num1*num2)
        i+=1
    elif "IFZERO" in text:
        wordlist=text.split()
        jump=int(wordlist[1])
        check=stack[-1]
        stack.pop()
        if check==0:
            i=jump
            continue
        else:
            i+=1 
            
        
    elif text=="DONE":
        print(str(stack[-1]))
        break
    
    
    

#Chris Rubio
#1530668

phrase = input()
normal = 0 
backward = len(phrase)-1
result = True  
while(normal<backward):
    if(phrase[normal]==' '):
        normal+=1
    elif(phrase[backward]==' '):
        backward-=1
    elif(phrase[normal]!=phrase[backward]):
        result = False
        break
    else:
        normal+=1
        backward-=1
if (result):
    print(phrase,"is a palindrome")
else:
    print(phrase, "is not a palindrome")
  

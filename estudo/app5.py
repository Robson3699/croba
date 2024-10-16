
pS='texto'
acerto=''

while True:

 tent=input("Digite a palavra secreta ou a letra: ").lower()
 if tent==pS:
    break
 if(tent in pS):
   acerto+=tent
 tE=''
 for i in pS:
  if(i in acerto):
   tE+=i
   
  else:
    tE+="*"
 print(tE)
 if(tE==pS):
  break
  
   
 

   


s=""
n=int(input())
a=0
b=1
if n==1:
   print(b)
else:   
   print(b,end=" ")
for i in range(n-1):
   c=a+b
   #print result
   s=s+str(c)+" "
   a=b
   b=c
print(s.strip())   
     

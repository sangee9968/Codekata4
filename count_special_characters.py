s=input()
c=0
for i in range(0,len(s)):
   if s[i].isalnum()==False and s[i]!=" ":
      c=c+1
print(c)      

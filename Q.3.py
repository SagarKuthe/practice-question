l1=[10,20,25,30,35]
l2=[40, 45, 60, 75, 90]
c=[]
for i in range(len(l1)):
    if(l1[i]%2!=0):
        c.append(l1[i])
        
for i in range(len(l2)):
    if(l2[i]%2==0):
        c.append(l2[i])
print(c)

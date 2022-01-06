s="MISSISSIPPI"
c=list(s)
d=[]
for i in range(0,len(c)):
    for j in range(0,len(c)):
        if c[i] not in d:
            d.append(c[i])
#print(d)
m=[]
D={}
for k in range(0,len(d)):
    f=0
    for l in range(0,len(c)):
        if d[k]==c[l]:
            f+=1
    m.append(f)
    D.update({d[k]:f})
#print(m)
print(D)



    			
    	

    
    		
    		
    	

    	
 
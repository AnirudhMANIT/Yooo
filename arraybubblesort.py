from array import *
vals=array('i',[7,9,1,6,8,54])
for i in range(5):
    for j in range(6-i-1):
        
        if vals[j]>vals[j+1]:
            
            temp=vals[j]
            vals[j]=vals[j+1]
            vals[j+1]=temp
        else:
            pass
print(vals)    

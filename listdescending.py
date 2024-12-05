
while (True):
    a=input("enter the name to be arragne in order :")
    z=[]
    mydict={}
    z.extend(a)
    for x in range(len(z)):        
        for y in range (len(z)):
            if(z[x]<z[y]):
                z[x],z[y]=z[y],z[x]
    for x in z:
        if(x in mydict.keys()):
            mydict[x]= mydict[x]+1
        else:
            mydict[x]=1

    print(mydict)






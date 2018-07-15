#----sorting----

list=[12,15,10,7,9,85]
print("List =",list,'sorted list=',sorted(list),"over")
for i in range (0,len(list)):
    for j in range (i,len(list)):
        if(list[i]>list[j]):
            t = list[i] 
            list[i] = list[j]
            list[j] = t
print (list)
            

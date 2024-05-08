def marge_Short(list1, list2):
    i=j=k=0
    arraylist=[]
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            arraylist.append(list1[i])
            i+=1
        else:
            arraylist.append(list2[j])
            j+=1
        k+=1
    
    while i<len(list1):
        arraylist.append(list1[i])
        i+=1
        k+=1
    while j<len(list2):
        arraylist.append(list2[j])
        i+=1
        j+=1
        
    return arraylist


list1=[1,3,5,7]
list2=[2,4,6,8]
x=marge_Short(list1, list2)
print(x)

    
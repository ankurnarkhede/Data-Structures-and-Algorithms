

# a = array; m=mid; l=lefthalf; r=righthalf

# def swap(a,x,y):
#     'swapping of a[x] and a[y]'
#     a[x],a[y]=a[y],a[x]


def MergeSort(a):
    "perform Merge sort on array a"
    if(len(a)>1):
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        MergeSort(l)
        MergeSort(r)
        Merge(a,m,l,r)

def Merge(a,m,l,r):
    # sort and merge the array
    i = j = k = 0
    while ((i<len(l)) and (j<len(r))):
        if(l[i]<r[j]):
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k += 1

    while(i<len(l)):
        a[k]=l[i]
        i+=1
        k+=1

    while (j < len (r)):
        a[k] = r[j]
        j += 1
        k += 1


# main
n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n,+1):
    a.append(int(input("Enter the %s th element:"%(i))))
print('Initial array     :',a)

MergeSort(a)

print('Merge sorted array:',a)


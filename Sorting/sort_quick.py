
# a = array;

def swap(a,x,y):
    'swapping of a[x] and a[y]'
    a[x],a[y]=a[y],a[x]

def Partition(a,low,high):
    "perform Quick sort on array a"
    pivot=low
    swap(a,pivot,high)
    for i in range(low, high,+1):
        if (a[i]<=a[high]):
            swap(a,i,low)
            low+=1
    swap(a,low,high)
    return low

def QuickSort(a,low,high):
    if(low<high):
        pi=Partition(a,low,high)
        QuickSort(a,low,pi-1)
        QuickSort(a,pi+1,high)

# main
n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n,+1):
    a.append(int(input("Enter the %s th element:"%(i))))
print('Initial array     :',a)

QuickSort(a,0,len(a)-1)

print('Quick sorted array:',a)


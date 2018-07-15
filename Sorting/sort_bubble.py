

def swap(a,x,y):
    'swapping of a[x] and a[y]'
    a[x],a[y]=a[y],a[x]
    # return a

def BubbleSort(a):
    "perform bubble sort on array a"
    for i in range(0,len(a),+1):
        for j in range(0, len(a)-i-1,+1):
            if(a[j]>a[j+1]):
                swap(a,j,j+1)


# main
n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n,+1):
    a.append(int(input("Enter an element:")))
print('Initial array:',a)

BubbleSort(a)

print('Bubble sorted array:',a)


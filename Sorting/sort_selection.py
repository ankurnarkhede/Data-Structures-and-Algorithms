

def swap(a,x,y):
    'swapping of a[x] and a[y]'
    a[x],a[y]=a[y],a[x]

def SelectionSort(a):
    "perform selection sort on array a"
    for i in range(0,len(a),+1):
        least=i
        for j in range(i+1,len(a),+1):
            if(a[j]<a[least]):
                swap(a,j,least)


# main
n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n,+1):
    a.append(int(input("Enter an element:")))
print('Initial array:',a)

SelectionSort(a)
print('##########PERFORMING SELECTION SORT##########')
print('Selection sorted array:',a)



# def swap(a,x,y):
#     'swapping of a[x] and a[y]'
#     a[x],a[y]=a[y],a[x]

def ShellSort(a):
    "perform Shell sort on array a"
    n=len(a)
    gap=n//2
    # print("gap=",gap)
    while gap > 0:
        for i in range(gap,n):
            temp=a[i]
            j=i

            while((j>=gap) and (a[j-gap]>temp)):
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap//=2

# main
n=int(input('Enter no of elements:'))
a=[]
for i in range(0,n,+1):
    a.append(int(input("Enter the %s th element:"%(i))))
print('Initial array     :',a)

ShellSort(a)

print('Shell sorted array:',a)


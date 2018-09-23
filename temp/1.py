# 4
# 1 4 2 3

import sys
import math
import hashlib

def is_perfect_square(n):
    return math.sqrt(n).is_integer ()

def get_md5(num):
    return hashlib.md5 (str (num).encode ()).hexdigest ()

def subarray_sum(arr):
    result=0
    for k in range(0,len(arr),+1):
        result+=arr[k]*(k+1)*(len(arr)-1)
    return result

def main():
    n=int (sys.stdin.readline ().strip ())

    arr = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    dict={}

    count=0
    for i in range(0,n,+1):
        for j in range(i+1,n+1,+1):
            print("({},{})".format(i,j))
            if(is_perfect_square(sum(arr[i:j]))):
                print(sum(arr[i:j]))
                count+=1

    print(count)


if __name__ == "__main__":
    main ()

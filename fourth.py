def sort_func(A,low,mid,high):
   
    while mid <= high:
        
        if A[mid] == 0:
            A[low],A[mid] = swap(A[low],A[mid])
            low = low + 1
            mid = mid + 1
        
        elif A[mid] == 2:
            A[mid],A[high] = swap(A[mid],A[high])
            high = high-1
        
        elif A[mid] == 1:
            mid = mid + 1
        print(A)

    return A

def swap(a,b):
    a,b = b,a
    return a,b

if __name__ == "__main__":
    
    A = [0,1,2,2,1,0,0,1]

    pp = sort_func(A,0,0,len(A)-1)

    print(pp)





# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def merge(X, Y):
    " merge two sorted lists "
    i = j = 0
    out = []
    while i < len(X) and j < len(Y):
        _min = min(X[i], Y[j])
        out.append(_min)
        if(_min==X[i]) : i+=1
        else: j+=1
    out += X[i:] + Y[j:]
    return out

def mergeSort(A):
    if len(A) <= 1:
        return A
    if len(A) == 2:
        return sorted(A)

    mid = len(A) // 2
    
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

from random import randint
if __name__ == "__main__":
    # Generate 20 random numbers and sort them
    A = [randint(1, 100) for i in range(20)]
    print (mergeSort(A))

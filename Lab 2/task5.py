#5a

array = [1,3,4,5,9,10,10]
def partition(array,p,q):
    p_v = array[p]
    x=p
    for y in range(p+1,q):
        if array[y]<=p_v:
            x=x+1
            array[x],array[y]=array[y],array[x]

    array[p]=array[x]
    array[x]=p_v
    return x

def quicksort(array,p,r):
    if r>p:
        q=partition(array,p,r)
        quicksort(array,p,q-1)
        quicksort(array,q+1,r)

quicksort(array,3,6)
print(array)


# worst_case O(n^2)
# average case O(nlogn)
# best case O(nlogn)


#5b

def findk(array,l,r,k):
    if l==r:
        return array[l]
    pos =partition(array,l,r)
    count = pos-l+1
    if count==k:
        return array[pos]
    elif k<count:
        return findk(array,l,pos-1,k)
    else:
        return findk(array,pos+1,r,k-l)

def partition(array,l,r):
    y = array[r]
    j=l-1
    for k in range(l,r-1):
        if array[k]<=y:
            j=j+1
            array[j],arr[k]=arr[k],arr[j]
    array[j+1], array[r] = array[r], array[j+1]


# worst_case O(n^2)
# average case O(n)
# best case O(n)

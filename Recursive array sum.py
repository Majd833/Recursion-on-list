def arraysum(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0] + arraysum(a[1:])
a=[1,2,3,4,5,6]
print('The total sum of the array is:',arraysum(a))
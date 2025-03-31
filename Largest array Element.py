def maxele(a):
    length=len(a)
    if length==1:
        return a[0]
    return max(a[0],maxele(a[1:]))
a=[1,78,46,96,2,6,58]
print('the largest element in the array is:',maxele(a))
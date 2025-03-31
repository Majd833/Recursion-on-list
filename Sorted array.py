def sorted(a):
    length=len(a)
    if length==1 or length==0:
        return True
    return a[0]<=a[1] and sorted(a[1:])
a= [1,2,3,4,5,6,7]
if sorted(a):
    print("The given array is sorted")
else:
    print("The given array isn't sorted")
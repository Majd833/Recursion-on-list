def lenlist(mylst):
    if not mylst:
        return 0
    return 1 + lenlist(mylst[1::2])+ lenlist(mylst[2::2])
mylst=[1,3,5,4,7,6,2,89,5,7,567]
print("the length of the array is:",lenlist(mylst))

def search(list,n):

    low=0
    upper=len(list)-1

    while low<=upper:
        mid=(low+upper)//2

        if list[mid]==n:
            return True
        else:
            if list[mid]<n:
                low= mid
            else:
                upper=mid
    return False

list=[1,4,6,8,10,13,17,21]
n=13

if search(list,n):
    print ("Found")
else:
    print("not found")

def search(list,key):

    low=0
    upper=len(list)-1

    while low<=upper:
        mid=(low+upper)//2

        if list[mid]==key:
            return True
        else:
            if list[mid]<key:
                low= mid+1
            else:
                upper=mid+1
    return False

list=[1,4,6,8,10,13,17,21]
n=13

if search(list,key):
    print ("Found")
else:
    print("not found")

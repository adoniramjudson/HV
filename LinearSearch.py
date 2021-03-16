#Method 1:
# def search(list,n):
#     i=0
#
#     while i<len(list):
#         if list[i]==n:
#             return True
#         i=i+1
#
#     return False
# list=[1,4,5,7,12,15,17,25]
# n=7
#
# if search (list,n):
#     print("Found")
# else:
#     print("Not Found")

#Method 2

def search(list, key):
    for i in range(len(list)):
        if list[i]==key:
            print ("Element is Found")
            break

    else:
        print("Element not found")

list=[12,14,15,16,20,25,28,30]
key= int(input("Enter the key element:"))
search(list,key)
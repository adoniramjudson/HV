arr = [1,4,6,7,9,15,17,18]
ele=9
flag=0
for i in arr:
    if (i==ele):
         print ("Element Exits")
         flag=1
         break
if (flag==0):
     print ("Element not found")

# arr= [1,4,6,7,9,15,17,18]
# ele =15
#
# if (ele in arr):
#     print("Element Found")
# else:
#     print("Element not found")
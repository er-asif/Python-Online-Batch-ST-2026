# num = int(input("Enter a number "))
# sq = num**2                         
# temp = num
# # digits = len(str(num))
# digits = 0                  
# while temp>0:
#     digits +=1
#     temp = temp // 10     

# if sq % 10**digits == num:        
#     print("Automorphic Number")
# else:
#     print("Not an Automorphic number")


# Using endswith method 

num = int(input("Enter a number ")) # 25
sq = str(num**2) # "625"

if sq.endswith(str(num)):
    print("Automorphic number")
else:
    print("Not automorphic")

    
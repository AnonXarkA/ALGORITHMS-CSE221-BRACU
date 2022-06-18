def square_count(a,b):
    count =0
    for x in range(a,b+1):
        k =1
        while x >= k*k:
            if k*k == x:
                count+=1
            k+=1
        x+=1
    return count


            #   Sample Input 
# 1 4
# 1 10
# 0 0 

print(square_count(1,4))
print(square_count(1,10))
print(square_count(0,0))

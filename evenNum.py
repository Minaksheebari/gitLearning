### take input from user
#print all the even numbers till that number eg. 10 then output is 2,4,6,8...
#print sum of all output numbers. 

num = int(input("Enter any positive number: "))
# print("Even numbers till ", num, "are: ")
 
#for loop 
sum = 0
for index in range(1,num+1,1):   
    if(index % 2 == 0):
        print(index)
        sum =sum + index      
print("Total sum of numbers: ",sum)

### while loop for 
# index = 1
# sum = 0
# while(index <= num):
#     if(index % 2 == 0):
#         print(index)
#         sum =sum + index
#     index=index+1               ##stage 1
# print("Total sum of numbers: ",sum)


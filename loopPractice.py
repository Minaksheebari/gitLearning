#take inputs - starting no. & ending no.
#eg 15-30
#use loop to print those numbers

startNumber = int(input("Enter starting number: "))
endNumber = int(input("Enter ending number: "))

print("Numbers between ", startNumber, "and", endNumber, "are: ")
#using while loop

# newNumb = startNumber
# while newNumb <= endNumber:
#     print(newNumb)
#     newNumb+=1

#using for loop
sum=0
for num in range(startNumber,endNumber+1):
    print(num)
    sum+=num
#addition of this range
print("Addition of all is: ",sum)

#check for even numbers in range and print addition
evenSum = 0
oddSum = 0

for num in range(startNumber,endNumber+1,1):
    if(num % 2 == 0):
        #print("Even Number = ",num)
        evenSum = evenSum + num
    elif(num != 0):
        #print("Odd Number: ", num)
        oddSum = oddSum + num
print("Addition of EVEN numbers: ", evenSum)    
print("Addition of ODD numbers: ", oddSum)  
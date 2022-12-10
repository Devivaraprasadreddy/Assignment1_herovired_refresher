# Assignment Question 1 Date:10-12-2022 Day:Saturday

# Take Input From Five Different Users

num1 = int(input("Please Enter The Number Of User1 : "))
num2 = int(input("Please Enter The Number Of User2 : "))
num3 = int(input("Please Enter The Number Of User3 : "))
num4 = int(input("Please Enter The Number Of User4 : "))
num5 = int(input("Please Enter The Number Of User5 : "))

# Condition : If any one user enter the value is zero (0) or less than zero. It will shown some error message like please enter a positive number
# using if-else condition 'if' condition is true it will print error message
# else condition it will print all values and print the total values

if(num1<=0 or num2<=0 or num3<=0 or num4<=0 or num5<=0):
    print("\nCondition : Please Enter A Positive Number")
    x=open("newdata.txt","a")
    x.write(str("Condition : Please Enter A Positive Number"))
    print("\n")
else:
    print("The Five Users Values are : ")
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num5)
# This part is considered  print the output in the console and as well as some text file


    x = open("newdata.txt","a")
    x.write(str("The Five Users Values are : "))
    x.write("\n")
    x.write(str("User1 : "))
    x.write(str(num1))
    x.write("\n")
    x.write(str("User2: "))
    x.write(str(num2))
    x.write("\n")
    x.write(str("User3 : "))
    x.write(str(num3))
    x.write("\n")
    x.write(str("User4 : "))
    x.write(str(num4))
    x.write("\n")
    x.write(str("User5 : "))
    x.write(str(num5))
    x.write("\n")
    total = num1+num2+num3+num4+num5
    x.write(str("The Total Value is : "))
    x.write(str(total))
    x.write(str("\n"))
    print("The Total Value is : ")
    print(total)
   
    

       
    
  
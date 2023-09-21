

#Backwards number 
"""user_input = (input("Enter Number:"))
number = user_input[::-1]
print(number)
"""
#Number AVG SUM PR
"""user_input = int(input("Enter Number:"))

dig1 = user_input // 1000
dig2 = (user_input // 100) % 10 
dig3 = (user_input // 10 ) % 10 
dig4 = user_input % 10 

sum_dig = dig1 + dig2 + dig3 + dig4
avg_dig = sum_dig / 4
p_dig = dig1 * dig2 * dig3 * dig4

print("Sum: ", sum_dig)
print("Avg: ", avg_dig)
print("P: ", p_dig)
"""
#Swap 2 digit values
"""user_input = int(input("Enter Number1:"))
user_input2 = int(input("Enter Number2:"))

temp = user_input 
user_input = user_input2
user_input2 = temp

print("a = ", user_input , "b = ", user_input2)"""

#Sum in interval [a b]
"""user_input = int(input("Enter Start Interval:"))
user_input2 = int(input("Enter End Interval:"))



sumarry = sum(range(user_input , user_input2 + 1))

print(sumarry)"""

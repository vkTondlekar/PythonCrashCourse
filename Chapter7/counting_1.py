"""
consider a loop that counts from 1 to 10 but prints only the odd numbers in that range.
"""
current_number = 0
while current_number < 10:
#we increment the count by 1
    current_number += 1
    if current_number % 2 == 0:
#if statement then checks the modulo of current_number and 2. If the modulo is 0
#continue statement tells Python to ignore the rest of the loop and return to the beginning
        continue
#If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number
    print(current_number)
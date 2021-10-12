### Conditional Statement

# age = int(input("What age are you?"))
# license = input("Do you have a provisional license? (Y/N)")
# if age >= 17:
#   if license == "Y":
#     print("Eligible")
#   else:
#     ("Not Eligible")
# else:
#   print("Not Eligible")

### Conditionals with Boolean

# age = int(input("What age are you?"))
# license = input("Do you have a provisional license? (Y/N)")
# if age >= 17 and license =="Y":
#   print("Eligible")
# elif age < 17:
#   print("Not eligible")
# else:
#   print("Not eligible")

# Write a program to ask the user their age and test score
# If the student is 16 or younger with a test result of 80 or higher, output should be "Excellent". 
# If student is over 16 with a test result of 80 or higher, output should read "good".
# If students scores less than 80, output should be "Try harder."

# Write a program for students where they input a percentage and the output is the grade.
# Take into account their level (H or O)
##################################

##  Nested loops - loops inside loops

# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")

# cols = 5
# for col in range(cols):
#   print("*", end = " ") #end = " " - stops  going to a new line after each star

# cols = 5
# rows = 4
# for row in range(rows):
#   for col in range(cols):
#     print("*", end = " ")
#   print()
######################
### Times tables
# timesTables = 2
# for i in range (1, 11):
#   ans = i * timesTables
#   print(timesTables, "X", i, " =", ans)

### Times tables using nested loops

# for ttables in range(1, 11):
#   for i in range(1, 11):
#     ans = i * ttables
#     print(ttables, "X", i, " =", ans)

 Create a nested loop that outputs a times table up to 12, up to a multiplier of 12

Write a program that asks a user for a number of columns andd a number of rows.
The output should be a grid of stars corresponding to their input.

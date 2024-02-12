# This program reads the swimming time, cycling time and running time of an user and displays
# the total time the user took to complete his triathlon. It also displays the award he has received
# or not receieved depending on various conditions.

# Read swim_time, cycle_time and run_time from user and cast it to integer
swim_time = int(input("Enter your time for swimming in minutes: "))
cycle_time = int(input("Enter your time for cycling in minutes:"))
run_time = int(input("Enter your time for running in minutes: "))

# Calculate total_time taken by user to complete his triathlon which is sum of all his individual times
# for swim, cycle and running
total_time = swim_time + cycle_time + run_time

# Display the total_time taken by the user to complete his triathlon
print("Total taken by you to complete the triathlon is: {} minutes".format(total_time))

# If total_time is greater than equal to 0 and less than equal to 100 display message the user has 
# award Provincial colours
if (total_time >=0 and total_time <= 100):
    print("Fantastic! You have been awarded Provincial Colours")    
# If total_time is greater than equal to 101 and less than equal to 105 display message the user has 
# award Provincial Half Colours
elif (total_time >= 101 and total_time <= 105):
    print("Great! You have been awarded Provincial Half Colours")
# If total_time is greater than equal to 106 and less than equal to 100 display message the user has 
# award Provincial Scroll
elif (total_time >= 106 and total_time <= 110):
    print("Well Done! You have been awarded Provincial Scroll")
# If none of the above conditions were satisfied display message to user that he has won no award
else:
    print("You did not get an award this time! But great effort!")
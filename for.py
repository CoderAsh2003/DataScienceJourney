# #Make a list of monthly expenses and find the total expenses of all the months

# expenses = [12000,12500,11000,13500,15000,50000,5000]
# sum = 0
# for i in range(len(expenses)):
#     sum += expenses[i]

# print("Total expenses: {}".format(sum))


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# Using for loop figure out how many times you got heads

count = 0

for i in range(len(result)):
    if result[i] == "heads":
        count+=1
    else:
        continue
print(count)

# 2 .Print square of all numbers between 1 to 10 except even numbers


for i in range(1,11):
    if i%2==0:
        continue
    else:
        square = i**2
        print("square of {} is {}" .format(i,square))

# Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

amount = int(input("Enter an expense amount"))
flag = 0
for i in range(len(expense_list)):
    if amount == expense_list[i]:

        if i == 0:
            print("The expense occured in January")
            flag=1
            break
        elif i == 1:
            print("The expense occured in February")
            flag=1
            break
        elif i == 2:
            print("The expense occured in March")
            flag=1
            break
        elif i == 3:
            print("The expense occured in April")
            flag=1
            break
        elif i == 4:
            print("The expense occured in May")
            flag=1
            break

if flag == 0:
    print("Expense hasnt occured in any of the months")

# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
miles=0
for i in range(5):
    print(f"You ran {i+1} miles")

    tired = input("Are you tired")
    if tired == "yes":
        break
    elif tired == "no":
        miles+=1
        continue
if miles == 5:
    print("Congratulations! You completed the race")

else:
    print("Nice Try, Don't try again")
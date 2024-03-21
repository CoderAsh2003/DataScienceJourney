#What i learnt new other than the usual

#round - It is a function used to round off an integer

#Example: Find the distance taken for a car to reach from Mangalore to Udupi if the time taken was 1 hr 15 mins and the speed was 70 kmh

speed = 76.5 
time = 1 + (15/60)
distance = speed*time
print("The distance taken to reach Udupi from Mangalore is: {} km".format(round(distance))) #95.625 will be converted to 96km

#round(var_name, no_of_digits(opt parameter))

# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,


# Explain
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

list = [2200,2350,2600,2130,2190]

#1.
print("Extra dollars spent in Feb compared to Jan is {}".format(str(list[1]-list[0])))

#2.
quarter = list[0]
for i in range(1,3):
    quarter += list[i]
print("Total expense in the first quarter of the year is {}".format(quarter))

#3.
for i in range(len(list)):
    if(list[i]==2000):
        print("Yes")
        break
    else:
        print('No')
        break

#4.
list.append(1980)
print("Updated monthly expense",*list,sep = ' ')
refund = 200
list[4] = list[4]-refund

print("list",*list,sep = ' ')
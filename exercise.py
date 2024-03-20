#Odd or even

number = int(input("Enter a number to check odd or even: "))

if number%2 == 0:
    print("even")

else:
    print("odd")



# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal
    
India = ["Mumbai", "Banglore", "Chennai", "Delhi"]
Pakistan = ["Lahore","Karachi","Islamabad"]
Bangladesh = ["Dhaka", "Khulna", "Rangpur"]

city = input("Enter a city: ")

if city in India:
    print("{} belongs to India".format(city))

elif city in Pakistan:
    print("{} belongs to Pakistan".format(city))

elif city in Bangladesh:
    print("{} belongs to Bangladesh".format(city))

city2 = input("Enter another city: ")

if city in India and city2 in India:
    print("{} and {} belong to the same country".format(city,city2))
elif city in Bangladesh and city2 in Bangladesh:
    print("{} and {} belong to the same country".format(city,city2))
elif city in Pakistan and city2 in Pakistan:
    print("{} and {} belong to the same country".format(city,city2))

else:
    print("They do not belong to the same country")
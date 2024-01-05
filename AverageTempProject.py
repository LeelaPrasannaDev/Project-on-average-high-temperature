'''
A project that takes higher temperatures of number of days 
and give the output as average of all the given temperatures 
and also tracking number of days is higher than the average temperature.

'''
# Asking user to enter how many days temperature average user want

numberOfDays = int(input("Enter number of days do you want the average of temperature = "))

#created a empty list to update later according to user input
temperatureList = []

#created a sum variable to track and add the all temperatures
sum = 0 

#created a loop in a range of number of days that the user enterd 
for i in range(0,numberOfDays):

    # Asking user to enter the temperature in days wise
    daysTemp = int(input("Enter {} day high temperature = ".format(i+1)))

    # user enterd temperature will be updated in the list days wise as indexs
    temperatureList.append(daysTemp)

    # caluclating the total sum of all the elements in the list or adding all the temperatures
    sum = sum+temperatureList[i]

# caluclating the average temperature 
avg = (sum)/len(temperatureList)

# average temperature will be converted to string formate and displaying to the user
print("The average temperature is = ",str(avg))


# to find number of days temperature is above average

# taking count variable to track the number of days is higher than the average temperature 
count = 0

# creating a loop to access all the temperature in the temperatureList
for i in temperatureList:

    # checking condition to find the temperatures which are higher than the average temperature
    if i > avg:
        count = count+1

print("{} day(s) is higher temperature than average temperature...".format(count))

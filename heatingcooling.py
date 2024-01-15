# last_name, first_name
# date
# Returns the running total of the numbner of heating and cooling days based on user input of average daily temperature

#Intializes the variables
average_daily_temperature = 0
heating_days = 0
cooling_days = 0

#Categorizes a given temperature as either a heating day or cooling day, or none at all
while average_daily_temperature >= -459: 
    average_daily_temperature = int(input("Enter the average daily temperature: "))
    if average_daily_temperature < -459:
        break
    elif average_daily_temperature < 60:
        heating_days+=1
    elif average_daily_temperature > 80:
        cooling_days+=1
    else:
        heating_days+=0
        cooling_days+=0

# Displays the number of heating and cooling days to the user
print("Heating days: ",heating_days)
print("Cooling days: ",cooling_days)

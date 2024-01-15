#Ask user for a speed limit and driving speed in miles per hour (mph)
speed_limit = int(input())
driving_speed = int(input())

#Output the traffic ticket amount
if driving_speed <= speed_limit - 10:
    print("50")
elif driving_speed >= speed_limit + 6 and driving_speed <= speed_limit + 20:
    print("75")
elif driving_speed >= speed_limit + 21 and driving_speed <= speed_limit + 40:
    print("150") 
elif driving_speed >= speed_limit + 40:
    print("300")
else:
    print("0")
phone_number = int(input())

last_four_numbers = phone_number % 10000
phone_number = phone_number // 10000

mid_three_numbers = phone_number % 1000
phone_number = phone_number // 1000

areacode = phone_number
print('(',areacode,')',mid_three_numbers,'-',last_four_numbers)
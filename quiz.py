print("Are you a tennis fanatic? Prove that you are the ultimate tennis fan by taking the quiz below!")
print("\n")
counter = 0
print("1. How many grand slam titles has Rafael Nadal won? Please enter a character for an answer (a, b, c, d, or e):\n a) 5\n b) 16\n c) 22\n d) 21\n e) 17")
answer_one = input(("Enter a character: "))
if answer_one == "c":
    print("You are correct! Rafael Nadal has won 22 grand slams.")
    counter += 1
else:
    print("Sorry, you are incorrect. The correct answer is c (22)!")
print("\n")
print("2. What was the fastest recorded serve (in mph) by a player in the 2023 US Open? Please enter an integer.")
answer_two = input("Enter your answer (in mph): ")
if answer_two == "147" :
    print("You are correct! Ben Shelton recorded the fastest serve at the 2023 US Open at 147 mph.")
    counter += 1
else:
    print("Sorry, you are incorrect. The correct answer is 147.")
print("\n")
print("3. It's the final question! Are you ready? TRUE or FALSE: Roger Federer won the 2019 Wimbledon Championships. Please enter TRUE or FALSE.")
answer_three = (input())
answer_three = answer_three.upper()
if answer_three == "TRUE":
    print("You are correct! Novak Djokovic defeated Roger Federer 7-6, 1-6, 7-6, 4-6, 13-2 in a thrilling final to win his 6th Wimbledon title and 20th major title overall.")
    counter += 1
else:
    print("Sorry, you are inncorect. Novak Djokovic defeated Roger Federer 7-6, 1-6, 7-6, 4-6, 13-2 in a thrilling final to win his 6th Wimbledon title and 20th major title overall.")

print("You scored ",counter, " questions correctly. Thanks for playing!")
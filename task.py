print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? rs"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% "))
people = int(input("How many people to split the bill? "))
t1=tip/100
total= bill*t1
t2= bill+total
split= t2/people
final= round(split,2)
print(f"final amount each person should pay: rs{final}" )


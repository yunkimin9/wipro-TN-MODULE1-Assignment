'''  project-1
Q-1 Create a python program that asks the user how far they want to travel. if they want
to travel less than three miles tell them to ride bicycle. of they want to travel more than three miles,
but less than three hundred miles, tell them to ride motor cycle.if they want to travel three hundred miles 
or more tell them to  drive super car '''

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("Use Bicycle to your destination.")
elif distance < 300:
    print(" Use Motor-Cycle to your destination.")
else:
    print("Use Super-Car to your destination.")


''' project-2
Q-2 Let's assume you are planning to use your python skills to build a PBLApp fpr mobile.
you decide to host your application on servers running in the cloud.
you pick a hosting provider that charges $0.51 per hour. you will launch your service using 
one server and want to know how much it will cost to operate per day,per week,per month.

'''

cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days_with_budget = budget / cost_per_day

print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for {days_with_budget:.2f} days.")
#this program takes input, coverts to numbers and totals the value
# a function is defined to get an input and convert to an int

def convert_string(str):
  return int(str)

def get_expense(msg):
  expense = int(raw_input(msg))
  return expense

test_string = "5"
print("Original:")
print(test_string * 2)

converted_string = convert_string(test_string)
print("Converted:")
print(converted_string * 2)

food_cost = get_expense("What's the cost of food?")
transport_cost = get_expense("What's the cost of transport?")
health_cost = get_expense("What is the cost to your health of living?")

total_cost = food_cost + transport_cost + health_cost

print("The total cost of living for you is " + str(total_cost))

raw_input("Press enter to exit")
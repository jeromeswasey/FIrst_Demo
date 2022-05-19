calculation_to_units = 24 #variables
name_of_unit = "hours" 


def days_to_units(num_of_days): #function
	return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
	

user_input = input("Hey user, enter a number of days and I will conver it to hours!\n")
user_input = int(user_input) #converts string to number (Casting called) int is built in python function
calculated_value = days_to_units(user_input)
print(calculated_value)



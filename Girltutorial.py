calculation_to_units = 24 #variables
name_of_unit = "hours" 


def days_to_units(num_of_days): #function
	print (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
	print ("All good!")

days_to_units(20)

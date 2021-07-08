'''

Property Tax

A county collects property taxes on the assessment value of property, which is 60 percent of the
property’s actual value. For example, if an acre of land is valued at $10,000, its assessment
value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. The tax for
the acre assessed at $6,000 will be $43.20. Write a program that asks for the actual value of a
piece of property and displays the assessment value and property tax.

'''

#constants
ASSESSMENT_FACTOR = .6
PROPERTY_FACTOR = .0072

#functions
def get_value():
	return float(input("What is the actual value of the property? "))
def assessment_value(real_value):
	return (real_value * ASSESSMENT_FACTOR)
def property_tax(assessment_value):
	return (assessment_value * PROPERTY_FACTOR)
def main():
	real_value = get_value()
	print("The assessment value of the property is: $" + format(assessment_value(real_value), '.2f'))
	print("The associated property tax is: $" + format(property_tax(assessment_value(real_value)), '.2f'))
main()
	
	


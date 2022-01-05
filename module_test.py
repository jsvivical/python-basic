import converter

print("enter a celcius value")
celcius = float(input())
fahrenheit = converter.convert_c_to_f(celcius)
print("That is %f fahrenheit degrees." % fahrenheit)

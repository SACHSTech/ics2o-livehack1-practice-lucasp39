"""
-------------------------------------------------------------------------------
Name:   f_to_c.py
Purpose:  Convert fahrenheit to celsius

Author: Pei.L

Created:  05/08/2021
------------------------------------------------------------------------------
"""
print ("****** Fahrenheit To Celsius Calculator ******")

#finding temperature in fahrenheit
fahrenheit = float(input("What is the temperature in Fahrenheit?: "))

#equation to convert f to c
celsius = ((fahrenheit-32)*(5/9))

#printing final conversion 
print ("The temperature in celcius is: "+str (celsius))
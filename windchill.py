"""
-------------------------------------------------------------------------------
Name:   windchill.py
Purpose:  Compute temperature in celsius after factoring windchill

Author: Pei.L

Created:  05/09/2021
-------------------------------------------------------------------------------
"""
print ("****** Windchill Calculator ******")

#find the temperature in celsius
temperature = float(input("What is the temperature in celsius?: "))
wind_speed = float(input("What is the wind speed in km/h?: "))

#calculate windchill factor
windchill = 13.12 + (.6215*temperature) - (11.37*wind_speed ** 0.16) + (.3965 * temperature*wind_speed ** 0.16)

#print windchill
print ("The temperature with windchill factored in is: " +str(round(windchill, 2)))
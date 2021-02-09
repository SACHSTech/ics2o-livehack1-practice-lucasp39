"""
-------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  Compute number of days and remaining hours from input of hours

Author: Pei.L

Created:  05/08/2021
------------------------------------------------------------------------------
"""
print ("****** Hours To Days ******")

#finding out number of hours
hours = int(input("How many hours?: "))

#calculating days and remaining hours
days = (hours//24)
remaining_hours = (hours%(days*24))

#print days and remaining hours
print (str(days) + " day(s) " + str(remaining_hours) + " hour(s)")
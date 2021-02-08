"""
-------------------------------------------------------------------------------
Name:   minutes_days.py
Purpose:  Compute number of days, hours, and minutes from input of minutes

Author: Pei.L

Created:  05/08/2021
------------------------------------------------------------------------------
"""

#find out number of minutes
minutes = int(input("How many minutes?: "))

#calculate days, hours, and remaining minutes
days = (minutes // 1440)
hours = (minutes//60 - days*24 )
remaining_minutes = minutes - (days * 1440) - (hours*60)

#print days, hours, and remaining minutes
print (str(days) + " days " +str(hours) + " hours " +str(remaining_minutes) + " minutes ")
# Author: John Asare
# Date: Sep 8 2018

# Copyright: Ownership right


""" This code is just a script/short code to help users keep track of their use of contact lenses. The code will
ask the user if he/she has used the contact lenses and then will remind them to throw it out when needed to"""


Days = 31

Ask = input("Are you wearing or going to wear your contacts today?:  ")
if Ask == "yes":
    Days -= 1
    print("\nAlright, after today, you have %d more days left to wear it." % Days)

else:
    print("\nAlright, you still have %d days left thought. Have fun and see better" % Days)





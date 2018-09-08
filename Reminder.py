# Author: John Asare
# Date: Sep 8 2018

# Copyright: Ownership right


""" This code is just a script/short code to help users keep track of their use of contact lenses. The code will
ask the user if he/she has used the contact lenses and then will remind them to throw it out when needed to"""


y = 31

x = input("Worn:? ")
if x == "yes":
    y -= 1
    print("You can wear your lenses for %d more days." % y)

else:
    print("Alright, you still have %s days left then. Have fun and see better" % y)





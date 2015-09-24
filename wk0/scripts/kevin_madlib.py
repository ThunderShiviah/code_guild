#Variables
name = input("Please type a name.\n >")
vehicle = input("Please input a type of vehicle.\n >")
food = input ("Please input a type of food.\n >")


story1 = (" was hungry one day and decided to to eat at a food ")
period = (".")
story3 = (" that sold ")
story4 = (" When {} ordered, however, the proprieter said, \"This is Portland, buddy! We only sell Kale!\"") .format(name)


print(name + story1 + vehicle + story3 + food + period + story4)

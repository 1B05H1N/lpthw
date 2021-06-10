name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds  heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight))

# These are all formatters, they tell python to take the variable on the right and put it in to replace the %s with its value:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

kgs = weight / 2.2 
cm = height * 2.54

print("%s weighs about %.0f kilos." % (name, kgs))
print("%s is about %0.f cm tall." % (name, cm))
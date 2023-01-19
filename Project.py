print("hello how are you today?")
print("We will now be commencing a game ")

name = input("What is your name?: ")
age = input("how old are you?: ")
year = input("What year were you born?: ")

profile = [name,
           age,
           year]

print(profile)

print("lets see how far you drove today")

mph = float(input("How many miles did you drive?"))
hours = float(input("How long did you drive?"))
distance = (mph * hours)
if distance <= 0:
    print("You did not drive anywhere!")
else:
    print = ("You drove" + str(distance) + "miles")

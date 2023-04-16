# Vergel, Chean Bernard V.
# Assignment No. 3
# Questions No. 2

# Create a header.
import pyfiglet
print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font = "digital" )
print(welcome)
print("")
print("=" * 80)
print("Hi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.")
print("")
# Ask for the name of the user.
name_of_user = input("How about you what is your name")
print("")
print("=" * 80)
print("")
# Make a greeting message for the user.
print("Good day,",name_of_user,"this program will ask you to input encrypted text and it will decrypt it by itself.")
print("")
# Ask if the user wants to continue.
agreement = str(input(Do you want to continue answering this program? Type YES if you want to continue and type NO if not."))
print("")
print("=" * 80)
print("")
# If user wants to continue, ask the user to input an encrypted text.
# If user don't want to continue, print thank you.
# Create a footer.

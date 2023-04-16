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
name_of_user = input("How about you what is your name? ")
print("")
print("=" * 80)
print("")
# Make a greeting message for the user.
print("Good day,",name_of_user,"this program will ask you to input encrypted text and it will decrypt it by itself.")
print("")
# Ask if the user wants to continue.
agreement = str(input("Do you want to continue answering this program? Type YES if you want to continue and type NO if not."))
print("")
print("=" * 80)
print("")
# If user wants to continue, ask the user to input an encrypted text.
if agreement.upper() == "YES":
    # ask the user to input an encrypted text
    print("Please encrypt your text using this guide 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !")
    print("")
    text = input("Please enter an encrypted text: ")
    encrypted_text = ""
    print("")
    print("Your encrypted text is: " + text)
    print("")
    print("Let us decrypt it.")
    print("")
# After inputing the encrypted text, ask user if want to decrypt it.
    agreement2 = str(input("Do you want to decrypt it? YES or NO: "))
# If user wants to decrypt it, do the calculations.    
    if agreement2.upper() == "YES":
           for e in text:
           # if *, change it to a 
            if e == '*':  
                 encrypted_text += 'a'
           # if &, change it to e
            elif e == '&':
                 encrypted_text += 'e'
           # if #, change it to i
            elif e == '#':
                 encrypted_text += 'i'
           # if +, change it to o
            elif e == '+':
                 encrypted_text += 'o'
           # if !, change it to u
            elif e == '!':
                 encrypted_text += 'u'
            else:
                 encrypted_text += e 
# Print output
    print("")
    print("DECRYPTED TEXT")
    print("The decrypted text of your input is:", encrypted_text)
    print("")
    print("Goodbye and thank you,",name_of_user,"have a nice day.")
# If user don't want to continue, print I hope you are doing well. Thank you for your time.
elif agreement.upper() == "NO":
    print("\033[32mI hope you are doing well. Thank you for your time",name_of_user +".\U0001F600\033[0m")
# If the response of the user is no, print I hope you are doing well. Thank you for your time.
else:
    print("\033[32mI hope you are doing well. Thank you for your time",name_of_user + ".\U0001F600\033[0m")   
# Create a footer.
print("")
print("=" * 80)
print("")
goodbye = pyfiglet.figlet_format("Visit me again", font = "puffy" )
print (goodbye)
print("")
print("=" * 80)
print("")
print("")

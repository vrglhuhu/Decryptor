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
print("\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m")
print("")
# Ask for the name of the user.
name_of_user = input("\033[35mHow about you what is your name?\U0001F917\033[0m ")
print("")
print("=" * 80)
print("")
# Make a greeting message for the user.
print("\033[23mGood day,",name_of_user,"this program will ask you to input encrypted text and it will decrypt it by itself.\033[0m")
print("")
# Ask if the user wants to continue.
agreement = str(input("\033[96mDo you want to continue answering this program? Type \033[0m\033[40m\033[33mYES\033[0m\033[96m if you want to continue and type \033[0m\033[40m\033[33mNO\033[0m\033[96m if not.\033[0m "))
print("")
print("=" * 80)
print("")
# If user wants to continue, ask the user to input an encrypted text.
if agreement.upper() == "YES":
    # ask the user to input an encrypted text
    print("\033[40m\033[33m\U0001F6CEPlease encrypt your text using this guide 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !\U0001F6CE\033[0m")
    print("")
    text = input("\033[95mPlease enter an encrypted text:\033[0m ")
    encrypted_text = ""
    print("")
    print("Your encrypted text is: " + text)
    print("")
    print("\033[40m\033[34mLet us decrypt it.\033[0m")
    print("")
# After inputing the encrypted text, ask user if want to decrypt it.
    agreement2 = str(input("Do you want to decrypt it? \033[40m\033[33mYES\033[0m or \033[40m\033[33mNO\033[0m: "))
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
    print("\033[41mDECRYPTED TEXT\U0001F447\033[0m")
    print("\n\033[35mThe decrypted text of your input is:\033[0m", encrypted_text)
    print("")
    print("\033[31mGoodbye and thank you,",name_of_user,"have a nice day.\U0001F600\033[0m")
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

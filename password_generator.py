from random import choice

while True:
    
    name = input ("welcome to the password generator, what's your nickname?: ")
    if name.isalpha() == True:
        print ("Hey " + name)
        break
    else:
        print (f"I don't think your name is {name}, can you tell me your real name?")
        continue
while True:
    try:
        n_password = int(input(f"how many characters do you want in your password: "))
        if n_password >= 101:
            print ("I don't think you'll remember, how about something shorter?")
        else:
            break
    except:
        print ("we do not accept letters as number XD")



pdrandom = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%"
password = ""
for x in range (n_password+1):
    password += choice(pdrandom)
print (f"your password is:\n{password}")
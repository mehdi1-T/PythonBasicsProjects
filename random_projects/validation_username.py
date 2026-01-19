def get_name():
    global username
    username = input("Enter your Username : ")

no_space = True if username.count(' ') == 0 else False
digit = True if username.isdigit() == False else False
lens = True if len(username) < 12 else False 

if no_space and digit and lens:
    print("You are welcome")
else:
    print("invalide username")
    try_again = input("Do you wanna try again : ")
    if try_again  == 'yes':
        get_name()
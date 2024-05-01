master_pwd = input("Enter your master password: ")

def add():
    name = input("Enter your Username: ")
    pwd = input("Enter your Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + '|' + pwd + "\n")
        # f.write("Username:" + name + ' | ' + "Password:" + pwd + "\n")

def view():
    with open("password.txt", "r") as f:
        # pwds = f.read()
        # print(pwds)
        for line in f.readlines():
            data = line.rstrip()
            user, pawd = data.split("|")
            print("Username: ", user, "|" , "Password: ", pawd)

while True:
    mode = input("Would you like to add or view password? (Add/View or q to quit): ").lower()
    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Enter valid input!")
    
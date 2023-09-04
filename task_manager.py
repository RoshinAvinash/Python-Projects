def user_info(usernm, passwd):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    txt_file = usernm + " task.txt"

    f = open(txt_file , "a")  
    f.write(f"{passwd}\n")
    f.write(f"--------------------------------------------------------------------------------------------------\n")
    f.write(f"Name: {name} \n")
    f.write(f"Address: {address} \n")
    f.write(f"Age: {age} \n")
    f.close()

def login():
    user_name = input("Enter your username: ")

    try:
        text_file = user_name + " task.txt"
        f_ = open(text_file,'r')
    
        pass_word = input("Enter your password: ")

        var = f_.readlines(0)[0].strip('\n')
        f_.close()
      
        
        if pass_word == var :
            print("Enter (1) or (2) for following operations: \n1-->To view your data \n2-->To add task")
        
            run = True
            while run:
                Operation = input()
                try:
                    Operation = int(Operation)
                    if Operation > 2 or Operation <1:
                        print("Choose correct number corressponding to required operation")
                    else:
                        run = False
                        if Operation == 1:
                            view_data(text_file)
                        elif Operation == 2:
                            task_add(text_file)

                except:
                    print("Enter a valid number")
                    
            
        else:
            print("Wrong password")
            login()
    except:
        print("File Not Found, Type correct user name")
        login()

def view_data(file):
    f1 = open(file,'r')
    #Prints everything in the file
    print(f1.read())
    f1.close()
    print("Thanks for using, work hard and see you again")

def task_add(file):
    run = True
    while run:
        f2 = open(file, "a")
        task = input("Enter the task: ")
        target = input("Enter the target: ")

        f2.write(f"Task is {task} and Target is {target}\n")

        s = input("If you want to stop press: spacebar and enter key OR if you want to add more press: enter key:")
        if s ==" ":
            run = False
            f2.close()
            press = input("Enter 1 if you want to view the tasks")
            if press == "1":
                view_data(file)
            else:
                print("Thanks for using, work hard and see you again")
                break
        else:
            continue

def signup():
    username = input("Please enter the username here: ")
    password = input("Enter a password:")
    user_info(username,password)
    print("Login please")
    login()

if __name__=='__main__':
    print("Welcome to the most Basic Task Manager")
    a = input("Choose 1 or 2: \n1-->If you want to sign up \n2-->If you want to login\n")

    if a =="1":
        signup()
    elif a =="2":
        login()
    else:
        print("Provide valide input")
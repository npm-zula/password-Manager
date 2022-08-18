from cryptography.fernet import Fernet

def key_write():
    mpass = "|aashiraftab"
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_f:
        key_f.write(key)
        key_f.write(mpass.encode())




def load_key():
    file = open('key.key')
    key = file.read()
    file.close()
    return key



def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.strip()
            user, pwd = data.split("|")
            print("User: " + user  + " Passowrd; " + fer.decrypt(pwd.encode()).decode())

def add():
    name = input("Enter the username:  ")
    passw = input("Enter the password:  ")

    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(passw.encode()).decode() + "\n")

key = load_key()
ekey, mpass = key.split("|")

master_pwd = input("Enter Master Password:  ")

if(mpass != master_pwd):
    quit()

mode = input("Do you want to add new password or view existing?  (view/ add) OR PRESS q to quit ")

fer =  Fernet(key)

while( mode != 'q'):

    if(mode == 'view'):
        view()

    elif(mode == 'add'):
        add()

    mode = input("Do you want to add new password or view existing?  (view/ add) OR PRESS q to quit ")
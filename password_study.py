
from cryptography.fernet import Fernet
global user,psw

#Run once to create the key.

'''def write_key() :  
    key=Fernet.generate_key()
    with open ("key.key", "wb") as kf :
        kf.write(key)

write_key() ''' 

#Loading the key

def load_key() :
    file=open("key.key", "rb")
    key=file.read()
    file.close()
    return key



key=load_key()
fer=Fernet(key)
def view() :
    nonlocal user,psw
    with open('password.txt', 'r') as f:
        for line in f.readlines() :
            data=line.rstrip()
            user,passw=data.split("|")
            psw=fer.decrypt(passw.encode()).decode()
            # print("User:",user,"| Password:",fer.decrypt(passw.encode()).decode())
def add(Ac_name,pwd) :

    with open('password.txt', 'a') as f:
        f.write(Ac_name+ "|"+fer.encrypt(pwd.encode()).decode()+"\n")
def clear() :
    with open('password.txt','w') as f:
        f.write('')
    print("\nCleared !")
